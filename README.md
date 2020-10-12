# ASL Compiler #
Compiler front end for C-like language ASL

Based on project completed in Compilers course CSE 4305. ASL is a purpose built language for that class and has nothing to do with ACPI Source Language.

Currently all but the last portion of the project has been pushed to this repository.

## Future of this project ##
Taken all together this compiler is a front end which is to say that this project takes written ASL code and transforms it into an Abstract Syntax Tree along with a Symbol Table which is the final step before code generation can begin. It exists as a detailed collection of elements that must be traversed to construct assembly code. 

This can be done using a tool such as [LLVM IR](https://llvm.org/docs/LangRef.html) which is a Intermediate Representation with mature tools surrounding it, importantly ones written in Python, that can be used to transform the AST into LLVM and subsequently transformed into assembly code.
