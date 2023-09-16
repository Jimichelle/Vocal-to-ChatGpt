# Speech to Text and ChatGPT Interaction

This Python code allows you to perform two main operations: converting an audio file to text and interacting with OpenAI's GPT-3 to generate text in response to a query.

## Usage

### Speech Recognition (Speech to Text)

1. Make sure you have installed the necessary libraries by running `pip install openai speech_recognition`.

2. Use the `recognition` function to convert an audio file to text. Here's how to use it:

```python
text = recognition("audio_file_name.wav")

The transcribed text will be displayed in the console and returned by the function.
