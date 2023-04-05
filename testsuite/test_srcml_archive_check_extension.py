import pylibsrcml

archive = pylibsrcml.srcMLArchive()

archive.register_file_extension("h","C++")

assert archive.check_extension("a.h") == "C++"
assert archive.check_extension("a.h.gz") == "C++"
assert archive.check_extension("a.foo") == None

archive.register_file_extension("foo","C++")
assert archive.check_extension("a.foo") == "C++"
assert archive.check_extension("a.foo.gz") == "C++"

try:
    archive.check_extension(0)
except pylibsrcml.srcMLTypeError:
    pass
