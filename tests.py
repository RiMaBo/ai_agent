from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file


def tests():
    # print("Result for current directory:")
    # print(get_files_info("calculator", "."))
    # print("")

    # print("Result for 'pkg' directory:")
    # print(get_files_info("calculator", "pkg"))
    # print("")

    # print("Result for '/bin' directory:")
    # print(get_files_info("calculator", "/bin"))
    # print("")

    # print("Result for '../' directory:")
    # print(get_files_info("calculator", "../"))
    # print("")


    # print("Result for 'calculator/lorem.txt' file:")
    # print(get_file_content("calculator", "lorem.txt"))
    # print("")

    # print("Result for 'calculator/main.py' file:")
    # print(get_file_content("calculator", "main.py"))
    # print("")

    # print("Result for 'calculator/pkg/calculator.py' file:")
    # print(get_file_content("calculator", "pkg/calculator.py"))
    # print("")

    # print("Result for '/bin/cat' file:")
    # print(get_file_content("calculator", "/bin/cat"))
    # print("")


    # print("Result for writing 'calculator/lorem.txt' file:")
    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    # print("")

    # print("Result for writing 'calculator/pkg/morelorem.txt' file:")
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print("")

    # print("Result for writing '/tmp/temp.txt' file:")
    # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    # print("")

    print("Result for running Python file 'calculator/main.py':")
    print(run_python_file("calculator", "main.py"))
    print("")

    print("Result for running Python file 'calculator/tests.py':")
    print(run_python_file("calculator", "tests.py"))
    print("")

    print("Result for running Python file '../main.py':")
    print(run_python_file("calculator", "../main.py"))
    print("")

    print("Result for running Python file 'calculator/nonexistent.py':")
    print(run_python_file("calculator", "nonexistent.py"))
    print("")


if __name__ == "__main__":
    tests()
