import boto3

text = """Translates input text from the source language to the target language. For a list of available languages and language codes, see what-is-languages ."""

client = boto3.client('translate')

response = client.translate_text(
    Text = text,
    SourceLanguageCode='en',
    TargetLanguageCode='fr',

)