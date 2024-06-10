import glfw
import numpy as np
import pyVulkan as vk
import ctypes
from gllt.linux.engine.base_widget import BaseWidget
from .signal import Signal


class Button(BaseWidget):
    def __init__(self, x, y, width, height, text, device, render_pass, pipeline_layout, pipeline):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.clicked = Signal()

        # Store Vulkan device and other Vulkan objects
        self.device = device
        self.render_pass = render_pass
        self.pipeline_layout = pipeline_layout
        self.pipeline = pipeline

        # Vertex buffer for the button quad
        self.vertex_buffer = self.create_vertex_buffer()

    def create_vertex_buffer(self):
        vertices = np.array([
            [self.x, self.y, 0.0],                       # Bottom-left
            [self.x + self.width, self.y, 0.0],          # Bottom-right
            [self.x + self.width, self.y + self.height, 0.0],  # Top-right
            [self.x, self.y + self.height, 0.0]          # Top-left
        ], dtype=np.float32)

        buffer_size = vertices.nbytes

        buffer_info = vk.VkBufferCreateInfo(
            sType=vk.VK_STRUCTURE_TYPE_BUFFER_CREATE_INFO,
            size=buffer_size,
            usage=vk.VK_BUFFER_USAGE_VERTEX_BUFFER_BIT,
            sharingMode=vk.VK_SHARING_MODE_EXCLUSIVE
        )

        vertex_buffer = vk.vkCreateBuffer(self.device, buffer_info, None)

        memory_requirements = vk.vkGetBufferMemoryRequirements(self.device, vertex_buffer)
        memory_allocate_info = vk.VkMemoryAllocateInfo(
            sType=vk.VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_INFO,
            allocationSize=memory_requirements.size,
            memoryTypeIndex=0  # This should be determined based on memory properties
        )

        vertex_buffer_memory = vk.vkAllocateMemory(self.device, memory_allocate_info, None)
        vk.vkBindBufferMemory(self.device, vertex_buffer, vertex_buffer_memory, 0)

        data_ptr = vk.vkMapMemory(self.device, vertex_buffer_memory, 0, buffer_size, 0)
        ctypes.memmove(data_ptr, vertices.tobytes(), buffer_size)
        vk.vkUnmapMemory(self.device, vertex_buffer_memory)

        return vertex_buffer

    def handle_mouse_event(self, button, state, x, y):
        if button == glfw.MOUSE_BUTTON_LEFT and state == glfw.PRESS:
            if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
                self.clicked.emit()

    def handle_key_event(self, key, x, y):
        pass

    def draw(self, command_buffer):
        vertex_buffers = [self.vertex_buffer]
        offsets = [0]
        vk.vkCmdBindPipeline(command_buffer, vk.VK_PIPELINE_BIND_POINT_GRAPHICS, self.pipeline)
        vk.vkCmdBindVertexBuffers(command_buffer, 0, 1, vertex_buffers, offsets)
        vk.vkCmdDraw(command_buffer, 4, 1, 0, 0)