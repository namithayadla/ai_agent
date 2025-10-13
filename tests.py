from functions.get_files_info import get_files_info
from functions.get_files_info import get_file_content
from functions.get_files_info import write_file
from functions.get_files_info import run_python_file
def run_tests():
    # print("Result for current directory:")
    # print(get_files_info("calculator", "."), "\n")

    # print("Result for 'pkg' directory:")
    # print(get_files_info("calculator", "pkg"), "\n")

    # print("Result for '/bin' directory:")
    # print(get_files_info("calculator", "/bin"), "\n")

    # print("Result for '../' directory:")
    # print(get_files_info("calculator", "../"), "\n")

    # print(get_file_content("calculator", "main.py"), "\n")
    # print(get_file_content("calculator", "pkg/calculator.py"), "\n")
    # print(get_file_content("calculator", "/bin/cat"), "\n")
    # print(get_file_content("calculator", "pkg/does_not_exist.py"), "\n")

    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"), "\n")
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"), "\n")
    # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"), "\n")

    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))
    print(run_python_file("calculator", "lorem.txt"))
if __name__ == "__main__":
    run_tests()