Very easy to crack, nevertheless provides two new concepts:

- structs: looks pretty transparent in assembler -> user space/programmer aid
- volatile variables

(reminder) volatile: retrieval of value can not be optimized and is always taken from hardware reg

A few things are still unclear regarding memory layout:
    - test if changme flag changed uses addr instead of value -> probably optimization
    - exactly when values are added and substracted from esp
