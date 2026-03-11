import re

class EmailClassifier:
    def __init__(self):
        # Define keywords for categories
        self.categories = {
            "Support": ["help", "issue", "problem", "not arrived", "error", "broken", "complaint", "support"],
            "Sales": ["price", "product", "purchase", "buy", "cost", "pricing", "quote", "interest"],
            "Spam": ["offer", "discount", "win", "prize", "free", "promotion", "subscribe", "limited time"],
            "General": ["hello", "hi", "greetings", "information", "thanks", "regards"]
        }
        
        # Define rules for priority
        self.urgent_keywords = ["urgent", "help", "complaint", "error", "broken", "not arrived", "immediately"]
        self.request_keywords = ["price", "question", "how", "what", "query", "product"]

    def preprocess(self, text):
        """
        Convert text to lowercase, remove punctuation, and tokenize.
        """
        text = text.lower()
        # Remove punctuation using regex
        text = re.sub(r'[^\w\s]', '', text)
        # Tokenize (simple split)
        tokens = text.split()
        return tokens

    def classify_category(self, text, tokens):
        """
        Classify email into a category based on keyword frequency.
        """
        scores = {cat: 0 for cat in self.categories}
        
        # Check for each keyword in the full text
        for cat, keywords in self.categories.items():
            for keyword in keywords:
                if keyword in text.lower():
                    scores[cat] += 1
        
        # Return the category with the highest score, default to General
        max_score = max(scores.values())
        if max_score == 0:
            return "General"
        
        return max(scores, key=scores.get)

    def detect_priority(self, category, text, tokens):
        """
        Determine urgency based on keywords and category.
        """
        # Rule-based priority
        if any(word in text.lower() for word in self.urgent_keywords) or category == "Support":
            return "High"
        elif any(word in text.lower() for word in self.request_keywords) or category == "Sales":
            return "Medium"
        else:
            return "Low"

    def generate_reply(self, category):
        """
        Generate a suggested reply template based on category.
        """
        replies = {
            "Support": "Thank you for reaching out. Our support team has received your request and will assist you shortly.",
            "Sales": "Thank you for your interest in our products! A sales representative will provide you with more information soon.",
            "Spam": "You have been unsubscribed from this list. Have a great day!",
            "General": "Hello! Thank you for your message. We have received it and will get back to if necessary."
        }
        return replies.get(category, "Thank you for your email.")

    def analyze(self, email_text):
        """
        Run the full analysis pipeline.
        """
        tokens = self.preprocess(email_text)
        category = self.classify_category(email_text, tokens)
        priority = self.detect_priority(category, email_text, tokens)
        reply = self.generate_reply(category)
        
        return {
            "category": category,
            "priority": priority,
            "suggestedReply": reply
        }
