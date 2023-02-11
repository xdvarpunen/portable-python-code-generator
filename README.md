# portable-python-code-generator

Offline first command line tool based Python code generation tool. Provide input and tool will provide output. Below instructions on how to get started using the tool.

---

Using [Daoguang/PyCodeGPT](https://github.com/microsoft/PyCodeGPT) to run Python code generator offline. Uses CPU instead of GPU.

> ## What is it?
> 
> PyCodeGPT is efficient and effective GPT-Neo-based model for python code generation task, which is similar to [OpenAI Codex](https://openai.com/blog/openai-codex/), [Github Copliot](https://copilot.github.com/), [CodeParrot](https://huggingface.co/blog/codeparrot), [AlphaCode](https://deepmind.com/blog/article/Competitive-programming-with-AlphaCode).

Created working example from [issue](https://github.com/microsoft/PyCodeGPT/issues/8)


## Getting Started

Guide made using Windows 11.

### Requirements

- ~Python version 3.7-3.9 (PyTorch limits)~
- Used Python version 3.10

### Venv

Refresher on Python virtual environment.

```powershell
python -m venv venv # Create virtual environment
.\venv\Scripts\activate # Activate virtual environment
deactivate # Deactivate virtual environment
```

## Running the application

```powershell
python -m pip install -r requirements.txt # Install dependencies if not installed yet
python main.py # Downloads PyTorch model if not downloaded yet and runs the app/script
```

### Example output 

```powershell
(venv) PS C:\Users\User\Documents\GitHub\portable-python-code-generator> python main.py
load generation pipeline from Daoguang/PyCodeGPT over, vocab size = 32000, eos id = 0, gpu device = 0.
Write prompt (example 'def say_hello():'): def say_hello():

    """
    A method to say hello to the terminal.
    """
    print(f"Hello, {request.remote_addr}!")

    print(f'Hello {user_name}!')

        global greeting, greeting_time
        greeting = greeting_time
        greeting_time = greeting

        message = "\n\nThis is a sample message from the amazinga game. What is your name?\n\nThe name is @",name
        print(message)
        say(message)

    print("hello world")

        say_hello_text = "Hello, World!"
        print(say_hello_text)
        user_input = int(input("Enter your Choice: "))
        if user_input == 0:
                print("Goodbye!")
                return
        elif user_input == 1:
                print("Hello!")
                return
        else:
                print("You have to enter a number from 0-4!")
                say_hello_text = input("Enter your Choice: ")
                if say_hello_text == "1":
                        print("Goodbye!")
                        return
                elif say_hello_text == "0":
                        print("Enter a number
```

```powershell
Write prompt (example 'def say_hello():'): create function that returns palindrom
ic
        palindromes that are within the range [0, n]
        """
        # Generate the palindromes
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if palindromes[mid] <= n:
                low = mid + 1
            else:
                high = mid - 1
        return palindromes[0]

    def _find_palindrome_in_range(self, n):
        """
        Finds the palindrome within a range [0, n]
        """
        # Find the index of the palindrome within
        # range [0, n]
        for i in range(len(
ic characters.
    def palindromic(self):
        # Write your code here
        pass
ic string
        try:
            # search for palindromic string in list of palindromic string
            for palindromic in self.palindromic:
                if palindromic in string:
                    return palindromic
        except:
            return None


    def build_palindromic_function(self, string, start, end):
        """
        builds a palindromic function according to the two rules
        """
        # build function that returns palindromic string
        # if the palindromic string starts with the string
        if string.startswith(start):
            # search for palindromic string
            for palindromic in self.palindromic:
                if
ic score, it will run twice for each case:
    # 1. A single test case, that does not exist in the database,
    # 2. A single test case, that does exist in the database,
    # 3. A single test case, that does exist in the database,
    # 4. A single test case, that does exist in the database,
    # 5. A single test case, that does exist in the database,
    # 6. A single test case, that does not exist in the database,
    # 7. A single test case, that does not exist in the database,
    # 8. A single test case, that does not exist in the database,
    # 9. A single test
ic string from given input string
```

---

> ## Reference
> If you want to use the models, you need to cite our following paper:
> 
> ```
> @inproceedings{CERT,
>   title={{CERT}: Continual Pre-training on Sketches for Library-oriented Code Generation},
>   author={Zan, Daoguang and Chen, Bei and Yang, Dejian and Lin, Zeqi and Kim, Minsu and Guan, Bei and Wang, Yongji and Chen, Weizhu and Lou, Jian-Guang},
>   booktitle={The 2022 International Joint Conference on Artificial Intelligence},
>   year={2022}
> }
> ```
