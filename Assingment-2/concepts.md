1. **API**
- Definition
  #### An API is a set of rules and protocols that allow different software applications to communicate and interact with each other.
- Purpose
   - Enables functionality sharing between applications.
   - Allows developers to build on existing platforms without reinventing the wheel.
   - Facilitates integration between software systems.
- Example
  - Google Maps API: Developers can embed Google Maps into their applications.

```python
import requests

# Use Google Maps API to get directions
response = requests.get("https://maps.googleapis.com/maps/api/directions/json", params={
    "origin": "New York",
    "destination": "Boston",
    "key": "YOUR_API_KEY"
})
print(response.json())
```
2. **SDK**
- Definition
   #### An SDK is a collection of tools, libraries, documentation, and code examples that help developers build software applications for a specific platform
- Purpose
   - Simplifies the development process for specific platforms or technologies.
   - Provides pre-built functionalities, so developers don’t need to code everything from scratch.
- Example
   - Android SDK: Helps developers create Android apps. It includes tools like Android Studio, libraries, and emulators.
```python
// Example of using Android SDK to create an activity
   public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
```
3. **Web APIs**
- Definition
  #### A Web API is an API accessed over the web using HTTP/HTTPS protocols, often providing data in JSON or XML format.
- Purpose
   - Allows applications to interact with remote servers over the internet.
   - Commonly used for web services like fetching or sending data.
- Example
  - Twitter API: Fetch tweets from Twitter.

```python
import requests

url = "https://api.twitter.com/2/tweets"
headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
params = {"ids": "123456789"}
response = requests.get(url, headers=headers, params=params)
print(response.json())
```
4. **Laibrary APIs**
- Definition
  #### A Library API is an API provided by a software library, allowing developers to use its functionalities in their code.
- Purpose
  - Simplifies programming by offering reusable components.
  - Reduces development time and ensures consistent behavior.
- Example
  - NumPy (Python): A library API for numerical computations.
```python
import numpy as np

# Example of using NumPy to calculate the mean
data = [1, 2, 3, 4, 5]
print(np.mean(data))
```
5. Prompting and Complition
- Definition prompting
 #### Prompting  refer to providing a prompt (input) to a machine learning model (like OpenAI’s GPT).
 
- Definition Complition
 #### Complition refers to receiving a completion (output or response).
- Purpose
  - Facilitates natural language interaction with AI models.
  - Used in chatbots, code generation, content creation, and more.
- Example
   - OpenAI GPT API for Text Completion:
```python
import openai

openai.api_key = "YOUR_API_KEY"
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Write a poem about the stars.",
    max_tokens=50
)
print(response.choices[0].text.strip())
```

