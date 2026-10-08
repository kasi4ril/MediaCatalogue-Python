class MediaError(Exception):
    """Custom exception for media-related errors."""
    
    def __init__(self, message, obj):
        # Call the base Exception constructor
        super().__init__(message)
        # Store the invalid object for debugging/logging purposes
        self.obj = obj

class Movie:
    
    """Parent class representing a movie."""
    
    def __init__(self, title, year, director, duration):
        # Validate inputs to ensure data integrity
        if not title.strip():
            raise ValueError('Title cannot be empty')
        if year < 1895: # 1895 marks the historical birth of cinema
            raise ValueError('Year must be 1895 or later')
        if not director.strip():
            raise ValueError('Director cannot be empty')
        if duration <= 0:
            raise ValueError('Duration must be positive')
        
        # Assign validated values to instance attributes
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration
    
    def __str__(self):
        # Magic method to provide a clean, human-readable string representation
        return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'

class TVSeries(Movie):

    """Child class representing an entire TV series. Inherits from Movie."""
    
    def __init__(self, title, year, director, duration, seasons, total_episodes):
        # Use super() to initialize attributes inherited from the Movie parent class
        super().__init__(title, year, director, duration)
        
        # Additional validation specific to TVSeries properties
        if seasons < 1:
            raise ValueError('Seasons must be 1 or greater')
        if total_episodes < 1:
            raise ValueError('Total episodes must be 1 or greater')
        
        # Assign TV-specific attributes
        self.seasons = seasons
        self.total_episodes = total_episodes
    
    def __str__(self):
        # Override the __str__ method for TVSeries to include season/episode metrics
        return f'{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}'

class MediaCatalogue:
    """A catalogue that can store different types of media items."""
    
    def __init__(self):
        # Initialize an empty list to aggregate media items
        self.items = []
    
    def add(self, media_item):
        # Restrict catalogue items strictly to Movie objects (or subclasses like TVSeries)
        if not isinstance(media_item, Movie):
            raise MediaError('Only Movie or TVSeries instances can be added', media_item)
        self.items.append(media_item)
    
    def get_movies(self):
        # List comprehension filtering for EXACTLY Movie objects
        # 'type(item) is Movie' prevents TVSeries from being included here
        return [item for item in self.items if type(item) is Movie]
    
    def get_tv_series(self):
        # List comprehension filtering for TVSeries objects
        # 'isinstance' is safe here since TVSeries is the target subclass
        return [item for item in self.items if isinstance(item, TVSeries)]
    
    def __str__(self):
        # Handle edge case where the catalogue has no items
        if not self.items:
            return 'Media Catalogue (empty)'
        
        # Separate items by category for organized output
        movies = self.get_movies()
        series = self.get_tv_series()
        
        result = f'Media Catalogue ({len(self.items)} items):\n\n'
        
        if movies:
            result += '=== MOVIES ===\n'
            # enumerate(..., 1) is used to start the numbering at 1 instead of 0
            for i, movie in enumerate(movies, 1):
                result += f'{i}. {movie}\n'
        
        if series:
            result += '=== TV SERIES ===\n'
            for i, item in enumerate(series, 1):
                result += f'{i}. {item}\n'
        
        return result

# --- Example Usage ---
catalogue = MediaCatalogue()

try:
    # Instantiate and add movies
    movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
    catalogue.add(movie1)
    movie2 = Movie('Inception', 2010, 'Christopher Nolan', 148)
    catalogue.add(movie2)
    
    # Instantiate and add TV series
    series1 = TVSeries('Scrubs', 2001, 'Bill Lawrence', 24, 9, 182)
    catalogue.add(series1)
    series2 = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62)
    catalogue.add(series2)
    
    # Print the formatted catalogue
    print(catalogue)
    
except ValueError as e:
    # Catch and print initialization validation errors (e.g., negative duration)
    print(f'Validation Error: {e}')
except MediaError as e:
    # Catch and print custom errors when adding unsupported object types
    print(f'Media Error: {e}')
    print(f'Unable to add {e.obj}: {type(e.obj)}')