class Printable: 
    class_var = 42

    def __str__(self):
        return f"The answer {self.class_var}"

print(Printable())
