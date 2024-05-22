__all__ = ['ConverterD2B']


class ConverterD2B:
    """
    A utility class for converting various data types to a bytearray.
    """

    @staticmethod
    def to_bytearray(data):
        """
        Converts various data types to a bytearray.

        Args:
            data: The data to be converted.

        Returns:
            bytearray: The converted data as a bytearray.

        Raises:
            ValueError: If the data type is not supported.
        """
        if isinstance(data, (bytes, bytearray)):
            return bytearray(data)
        elif isinstance(data, str):
            return bytearray(data, 'utf-8')
        elif isinstance(data, (int, float)):
            return bytearray(str(data), 'utf-8')
        else:
            try:
                return bytearray(data)
            except Exception as e:
                raise ValueError(f"Unsupported data type: {type(data)}") from e


if __name__ == '__main__':
    # Пример использования:
    # Преобразование строки в bytearray
    data_str = "Hello, world!"
    byte_array_from_str = ConverterD2B.to_bytearray(data_str)
    print(byte_array_from_str)

    # Преобразование списка в bytearray
    data_list = [1, 2, 3, 4, 5]
    byte_array_from_list = ConverterD2B.to_bytearray(data_list)
    print(byte_array_from_list)

    # Преобразование числа в bytearray
    data_number = 12345
    byte_array_from_number = ConverterD2B.to_bytearray(data_number)
    print(byte_array_from_number)
