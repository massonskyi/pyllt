import ctypes
import glfw
import pyVulkan as vk
from gllt.win.engine.base_widget import BaseWidget
from gllt.win.widgets.button import Button


class TllMainWindow:
    def __init__(self, title, width, height):
        self.width = width
        self.height = height
        self.widgets = []

        if not glfw.init():
            raise Exception("Failed to initialize GLFW")

        glfw.window_hint(glfw.CLIENT_API, glfw.NO_API)
        self.window = glfw.create_window(width, height, title, None, None)
        if not self.window:
            glfw.terminate()
            raise Exception("Failed to create GLFW window")

        self.instance = self.create_instance()
        self.surface = self.create_surface()
        self.device, self.graphics_queue, self.physical_device = self.create_device_and_queues()
        self.render_pass = self.create_render_pass()
        self.pipeline, self.pipeline_layout = self.create_pipeline()

    def create_instance(self):
        app_info = vk.VkApplicationInfo(
            sType=vk.VK_STRUCTURE_TYPE_APPLICATION_INFO,
            pApplicationName='Hello Vulkan',
            applicationVersion=vk.VK_MAKE_VERSION(1, 0, 0),
            pEngineName='No Engine',
            engineVersion=vk.VK_MAKE_VERSION(1, 0, 0),
            apiVersion=vk.VK_API_VERSION_1_0
        )

        # Get the required GLFW extensions
        extension_names = glfw.get_required_instance_extensions()
        if not extension_names:
            raise Exception("Failed to get required GLFW extensions")

        print("Required extensions:", extension_names)

        create_info = vk.VkInstanceCreateInfo(
            sType=vk.VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO,
            pApplicationInfo=app_info,
            enabledExtensionCount=len(extension_names),
            ppEnabledExtensionNames=extension_names
        )

        instance = vk.vkCreateInstance(create_info, None)
        if instance is None:
            raise Exception("Failed to create Vulkan instance")

        return instance

    def create_surface(self):
        if glfw.vulkan_supported():
            print("GLFW supports Vulkan")

            surface = glfw.create_window_surface(self.instance, self.window, None)
            if not surface:
                raise Exception("Failed to create window surface")
        else:
            raise Exception("GLFW does not support Vulkan")
        return surface

    def create_device_and_queues(self):
        physical_devices = vk.vkEnumeratePhysicalDevices(self.instance)
        if not physical_devices:
            raise Exception("Failed to find GPUs with Vulkan support")
        physical_device = physical_devices[0]

        queue_family_properties = vk.vkGetPhysicalDeviceQueueFamilyProperties(physical_device)
        queue_family_index = next(
            i for i, q in enumerate(queue_family_properties) if q.queueFlags & vk.VK_QUEUE_GRAPHICS_BIT
        )

        queue_priority = 1.0
        queue_create_info = vk.VkDeviceQueueCreateInfo(
            sType=vk.VK_STRUCTURE_TYPE_DEVICE_QUEUE_CREATE_INFO,
            queueFamilyIndex=queue_family_index,
            queueCount=1,
            pQueuePriorities=[queue_priority]
        )

        device_create_info = vk.VkDeviceCreateInfo(
            sType=vk.VK_STRUCTURE_TYPE_DEVICE_CREATE_INFO,
            queueCreateInfoCount=1,
            pQueueCreateInfos=[queue_create_info]
        )

        device = vk.vkCreateDevice(physical_device, device_create_info, None)
        if device is None:
            raise Exception("Failed to create logical device")

        graphics_queue = vk.vkGetDeviceQueue(device, queue_family_index, 0)
        return device, graphics_queue, physical_device

    def create_render_pass(self):
        color_attachment = vk.VkAttachmentDescription(
            format=vk.VK_FORMAT_B8G8R8A8_UNORM,
            samples=vk.VK_SAMPLE_COUNT_1_BIT,
            loadOp=vk.VK_ATTACHMENT_LOAD_OP_CLEAR,
            storeOp=vk.VK_ATTACHMENT_STORE_OP_STORE,
            stencilLoadOp=vk.VK_ATTACHMENT_LOAD_OP_DONT_CARE,
            stencilStoreOp=vk.VK_ATTACHMENT_STORE_OP_DONT_CARE,
            initialLayout=vk.VK_IMAGE_LAYOUT_UNDEFINED,
            finalLayout=vk.VK_IMAGE_LAYOUT_PRESENT_SRC_KHR
        )

        color_attachment_ref = vk.VkAttachmentReference(
            attachment=0,
            layout=vk.VK_IMAGE_LAYOUT_COLOR_ATTACHMENT_OPTIMAL
        )

        subpass = vk.VkSubpassDescription(
            pipelineBindPoint=vk.VK_PIPELINE_BIND_POINT_GRAPHICS,
            colorAttachmentCount=1,
            pColorAttachments=[color_attachment_ref]
        )

        render_pass_info = vk.VkRenderPassCreateInfo(
            sType=vk.VK_STRUCTURE_TYPE_RENDER_PASS_CREATE_INFO,
            attachmentCount=1,
            pAttachments=[color_attachment],
            subpassCount=1,
            pSubpasses=[subpass]
        )

        render_pass = vk.vkCreateRenderPass(self.device, render_pass_info, None)
        if render_pass is None:
            raise Exception("Failed to create render pass")

        return render_pass

    def create_pipeline(self):
        vert_shader_code = open('vert.spv', 'rb').read()
        frag_shader_code = open('frag.spv', 'rb').read()

        vert_shader_module = self.create_shader_module(vert_shader_code)
        frag_shader_module = self.create_shader_module(frag_shader_code)

        vert_shader_stage_info = vk.VkPipelineShaderStageCreateInfo(
            sType=vk.VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_CREATE_INFO,
            stage=vk.VK_SHADER_STAGE_VERTEX_BIT,
            module=vert_shader_module,
            pName='main'
        )

        frag_shader_stage_info = vk.VkPipelineShaderStageCreateInfo(
            sType=vk.VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_CREATE_INFO,
            stage=vk.VK_SHADER_STAGE_FRAGMENT_BIT,
            module=frag_shader_module,
            pName='main'
        )

        shader_stages = [vert_shader_stage_info, frag_shader_stage_info]

        vertex_input_info = vk.VkPipelineVertexInputStateCreateInfo(
            sType=vk.VK_STRUCTURE_TYPE_PIPELINE_VERTEX_INPUT_STATE_CREATE_INFO
        )

        input_assembly = vk.VkPipelineInputAssemblyStateCreateInfo(
            sType=vk.VK_STRUCTURE_TYPE_PIPELINE_INPUT_ASSEMBLY_STATE_CREATE_INFO,
            topology=vk.VK_PRIMITIVE_TOPOLOGY_TRIANGLE_LIST,
            primitiveRestartEnable=False
        )

        viewport = vk.VkViewport(
            x=0.0, y=0.0,
            width=800, height=600,
            minDepth=0.0, maxDepth=1.0
        )

        scissor = vk.VkRect2D(
            offset=vk.VkOffset2D(x=0, y=0),
            extent=vk.VkExtent2D(width=800, height=600)
        )

        viewport_state = vk.VkPipelineViewportStateCreateInfo(
            sType=vk.VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_STATE_CREATE_INFO,
            viewportCount=1,
            pViewports=[viewport],
            scissorCount=1,
            pScissors=[scissor]
        )

        rasterizer = vk.VkPipelineRasterizationStateCreateInfo(
            sType=vk.VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_STATE_CREATE_INFO,
            depthClampEnable=False,
            rasterizerDiscardEnable=False,
            polygonMode=vk.VK_POLYGON_MODE_FILL,
            lineWidth=1.0,
            cullMode=vk.VK_CULL_MODE_BACK_BIT,
            frontFace=vk.VK_FRONT_FACE_CLOCKWISE,
            depthBiasEnable=False
        )

        multisampling = vk.VkPipelineMultisampleStateCreateInfo(
            sType=vk.VK_STRUCTURE_TYPE_PIPELINE_MULTISAMPLE_STATE_CREATE_INFO,
            sampleShadingEnable=False,
            rasterizationSamples=vk.VK_SAMPLE_COUNT_1_BIT
        )

        color_blend_attachment = vk.VkPipelineColorBlendAttachmentState(
            colorWriteMask=(
                vk.VK_COLOR_COMPONENT_R_BIT |
                vk.VK_COLOR_COMPONENT_G_BIT |
                vk.VK_COLOR_COMPONENT_B_BIT |
                vk.VK_COLOR_COMPONENT_A_BIT
            ),
            blendEnable=False
        )

        color_blending = vk.VkPipelineColorBlendStateCreateInfo(
            sType=vk.VK_STRUCTURE_TYPE_PIPELINE_COLOR_BLEND_STATE_CREATE_INFO,
            logicOpEnable=False,
            logicOp=vk.VK_LOGIC_OP_COPY,
            attachmentCount=1,
            pAttachments=[color_blend_attachment],
            blendConstants=[0.0, 0.0, 0.0, 0.0]
        )

        pipeline_layout_info = vk.VkPipelineLayoutCreateInfo(
            sType=vk.VK_STRUCTURE_TYPE_PIPELINE_LAYOUT_CREATE_INFO
        )

        pipeline_layout = vk.vkCreatePipelineLayout(self.device, pipeline_layout_info, None)
        if pipeline_layout is None:
            raise Exception("Failed to create pipeline layout")

        pipeline_info = vk.VkGraphicsPipelineCreateInfo(
            sType=vk.VK_STRUCTURE_TYPE_GRAPHICS_PIPELINE_CREATE_INFO,
            stageCount=len(shader_stages),
            pStages=shader_stages,
            pVertexInputState=vertex_input_info,
            pInputAssemblyState=input_assembly,
            pViewportState=viewport_state,
            pRasterizationState=rasterizer,
            pMultisampleState=multisampling,
            pColorBlendState=color_blending,
            layout=pipeline_layout,
            renderPass=self.render_pass,
            subpass=0,
            basePipelineHandle=None,
            basePipelineIndex=-1
        )

        pipeline = vk.vkCreateGraphicsPipelines(self.device, vk.VK_NULL_HANDLE, 1, pipeline_info, None)
        if pipeline is None:
            raise Exception("Failed to create graphics pipeline")

        vk.vkDestroyShaderModule(self.device, vert_shader_module, None)
        vk.vkDestroyShaderModule(self.device, frag_shader_module, None)

        return pipeline, pipeline_layout

    def create_shader_module(self, code):
        create_info = vk.VkShaderModuleCreateInfo(
            sType=vk.VK_STRUCTURE_TYPE_SHADER_MODULE_CREATE_INFO,
            codeSize=len(code),
            pCode=code
        )
        shader_module = vk.vkCreateShaderModule(self.device, create_info, None)
        if shader_module is None:
            raise Exception("Failed to create shader module")
        return shader_module



window = TllMainWindow("Example Vulkan Window", 800, 600)
widget = Button(100, 100, 200, 50, "Hello World", window.device, window.render_pass, window.pipeline_layout, window.pipeline)
window.add_widget(widget)
window.main_loop()