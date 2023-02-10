# portable-python-code-generator

Using [Daoguang/PyCodeGPT](https://github.com/microsoft/PyCodeGPT) to run Python code generator offline. Uses CPU instead of GPU.

Created working example from [issue](https://github.com/microsoft/PyCodeGPT/issues/8)

## Getting Started

Guide made using Windows 11.

### Requirements

- Python version 3.7-3.9 (PyTorch limits)

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
(venv) PS C:\Users\User\Documents\GitHub\portable-python-chat-gpt> python main.py
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
