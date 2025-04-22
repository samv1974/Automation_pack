import re # regular expression model to identify email patterns

def extract_emails(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        # Regex pattern for matching emails
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, text)

        # Remove duplicates by converting to set and back to list
        unique_emails = sorted(set(emails))

        # Save the emails to output file
        with open(output_file, 'w', encoding='utf-8') as file:
            for email in unique_emails:
                file.write(email + '\n')

        print(f"✅ {len(unique_emails)} unique email(s) extracted to '{output_file}'")

    except FileNotFoundError:
        print(f"❌ File '{input_file}' not found.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

# Example usage:
extract_emails("sample.txt", "emails.txt")
