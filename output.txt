from classifier import EmailClassifier

def main():
    print("=== AI Email Classification & Auto-Reply System ===")
    print("Type 'exit' or 'quit' to stop.")
    
    classifier = EmailClassifier()
    
    while True:
        email_input = input("\nEnter Email Text: ").strip()
        
        if email_input.lower() in ['exit', 'quit']:
            break
            
        if not email_input:
            continue
            
        # Perform analysis
        result = classifier.analyze(email_input)
        
        # Display results
        print("\nAI Analysis Result:")
        print(f"Category: {result['category']}")
        print(f"Priority: {result['priority']}")
        print(f"Suggested Reply: {result['suggestedReply']}")

if __name__ == "__main__":
    main()
