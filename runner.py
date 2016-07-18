from processor import Processor

file_name = "program_samples\hello.hex"

processor = Processor(file_name)
processor.load()
processor.run()

if __name__ == '__main__':
    pass
