# Sikai Sellers CIS261 MovieGuidePart1

def display_menu():
    print("\nThe Movie List Program")
    print("\nCOMMAND MENU")
    print("list - List all movies")
    print("add  - Add a movie")
    print("del  - Delete a movie")
    print("exit - Exit the program")

def initialize_movies():
    return ["Paid in Full", "Step Brothers", "Belly"]

def list_movies(movies):
    if not movies:
        print("No movies to display.")
    else:
        for idx, movie in enumerate(movies, start=1):
            print(f"{idx}. {movie}")

def add_movie(movies):
    movie = input("Movie: ")
    movies.append(movie)
    print(f"{movie} was added.")

def delete_movie(movies):
    try:
        index = int(input("Number: ")) - 1
        if 0 <= index < len(movies):
            removed = movies.pop(index)
            print(f"{removed} was deleted.")
        else:
            print("Invalid movie number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    movies = initialize_movies()
    display_menu()

    while True:
        command = input("\nCommand: ").lower()
        if command == "list":
            list_movies(movies)
        elif command == "add":
            add_movie(movies)
        elif command == "del":
            delete_movie(movies)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.")

main()


