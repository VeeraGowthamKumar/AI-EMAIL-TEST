from classifier import EmailClassifier

def test_classifier():
    classifier = EmailClassifier()
    test_cases = [
        ("Hello, my order has not arrived yet. Please help.", "Support", "High"),
        ("What is the price of the premium product?", "Sales", "Medium"),
        ("Win a free prize now! Special offer discount.", "Spam", "Low"),
        ("Hello, hope you are doing well.", "General", "Low")
    ]
    
    all_passed = True
    for text, exp_cat, exp_pri in test_cases:
        res = classifier.analyze(text)
        if res["category"] != exp_cat or res["priority"] != exp_pri:
            print(f"FAILED: {text} -> got {res['category']}/{res['priority']}, expected {exp_cat}/{exp_pri}")
            all_passed = False
    
    if all_passed:
        print("VERIFICATION_SUCCESS")
    else:
        print("VERIFICATION_FAILED")

if __name__ == "__main__":
    test_classifier()
