import pyshorteners
import pyperclip  

def shorten_url():
    print("\n--- URL SHORTENER TOOL ---\n") 
    url = input("Enter your long URL: ")


    shortener = pyshorteners.Shortener()

    print("\nChoose shortening service:")
    print("1. TinyURL")
    print("2. is.gd")
    print("3. da.gd")

    choice = input("\nEnter your choice (1/2/3): ")

    try:
        if choice == "1":
            short_url = shortener.tinyurl.short(url)
        elif choice == "2":
            short_url = shortener.isgd.short(url)
        elif choice == "3":
            short_url = shortener.dagd.short(url)
        else:
            print("Invalid choice! Using TinyURL by default.")
            short_url = shortener.tinyurl.short(url)

        print("\n✅ Shortened URL:", short_url)

        
        copy_choice = input("\nDo you want to copy the URL to clipboard? (y/n): ").lower()
        if copy_choice == "y":
            pyperclip.copy(short_url)
            print("📋 Shortened URL copied to clipboard!")

    except Exception as e:
        print("\n❌ Error:", e)
        print("Please check your internet connection or the URL entered.")

while True:
    shorten_url()
    again = input("\nDo you want to shorten another URL? (y/n): ").lower()
    if again != "y":
        print("\nThank you for using the URL Shortener! 🔗")
        break
