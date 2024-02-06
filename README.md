# Wikipedia API Documentation

This API interacts with Wikipedia to perform specific text analysis tasks. It consists of two primary endpoints designed to analyze and store the frequency of words in Wikipedia articles based on user queries.

## Endpoints

### Word Frequency Analysis Endpoint

#### Functionality
- Accepts two parameters: `topic` (a string representing the subject of a Wikipedia article) and `n` (an integer specifying the number of top frequent words to return).
  
#### Process
- Fetches the text of the Wikipedia article corresponding to the provided topic.
- Analyzes the text to determine the frequency of each word.
- Returns the top `n` most frequent words in a structured format.

#### Implementation Details
- Implemented using FastAPI framework for building APIs in Python.
- Utilizes Pydantic models for request and response validation.

### Search History Endpoint

#### Functionality
- Lists the past search results, including the topics searched and the corresponding top frequent words returned by the API.

#### Implementation Details
- Implemented using FastAPI framework.
- Utilizes Pydantic models for request and response validation.

## Logic Explanation

- **Case Sensitivity**: The API handles case sensitivity by converting all text to lowercase before performing analysis. This ensures consistency in word counts.

- **Dynamic Content**: The API retrieves the latest version of Wikipedia articles to ensure that analysis reflects current content.

- **Namespace Filtering**: Content can be filtered based on namespaces to focus on relevant text and avoid unnecessary data. This helps improve the accuracy of word frequency analysis.

- **Title and Redirects**: The API handles redirects and variations in page titles to ensure it analyzes the intended content. This is achieved by resolving redirects and normalizing titles before analysis.

## Edge Cases

- **Empty Topic**: If the provided topic parameter is empty or not provided, the API returns an appropriate error response indicating that the topic is required.

- **Invalid Topic**: If the provided topic does not correspond to a valid Wikipedia article, the API returns an error indicating that the topic could not be found.

- **Negative or Zero `n`**: If the `n` parameter is negative or zero, the API returns an error indicating that `n` must be a positive integer.

- **Invalid Namespace Filter**: If the provided namespace filter is invalid or not recognized, the API returns an error indicating that the namespace filter must be a list of valid namespaces.

### Please refer to http://localhost:5069/docs#/ for documentaion of fastApi app.
  Note - Start the app before directing to above link.
