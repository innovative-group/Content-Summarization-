
# Project Title
[Content Summarizer] 

This is an AI powered Text/Content Summarizer web app developed on Python and Flask.



## Screenshots
![Gif  Text-Summarizer](https://github.com/innovative-group/Content-Summarization-/assets/51012877/545f7f64-28b0-4203-b971-8dd6f7249c2b)



## Documentation
Object Detection & Counting:
----------------------------
It is a simple AI powered Text/Content Summarizer web app developed on Python and Flask.

This web app will generate summary of your entered text in a simple and faster way.
Which will you to get good insight of your content in short time.


imports used:
-----------------------------
1> import spacy,
2> from spacy.lang.en.3> stop_words import STOP_WORDS
4> from string import punctuation
5> from heapq import nlargest
    
Some function you should be aware of 
----------------------------------
    1> .get() 
    2> .get
    3>  nlargest() 

        1> .get(): It is a method: It is a built-in method provided by dictionaries in Python.
                It is used to retrieve the value associated with a specified key in
                the dictionary. The method is called with parentheses and can take
                an optional default value parameter.

        2> .get :  It is an attribute: It refers to the underlying '.get()' method 
                itself without invoking it. It can be accessed without using 
                parentheses, and you can assign it to a variable or pass it as an
                argument to other functions.

        Example: 
        --------
        person = {'name': 'John', 'age': 30}

        name_1 = person.get('name')
        print(name_1)  # --->  Output: John

        get_method = person.get
        name_2 = get_method('name')
        print(name_2)  # --->  Output: John
    


 nlargest(n, iterable, key)    
        
        The nlargest function from the heapq module is used to retrieve then largest
        elements from a given iterable based on a specified key. The elements are 
        determined to be the largest based on the comparison of the values generated
        by the key function.
            
            n        : The number of largest elements to retrieve.
            iterable : The iterable from which the largest elements will be selected.  
            key      : The key parameter allows you to define a function that will be 
                    applied to each element in the iterable to generate a value for
                    comparison. The nlargest function then selects the n largest 
                    elements based on these generated values.



        First of all lets take/select a length of sentence that how many sentence 
        do we goona generate as summary output and we select sentence from "sent_freq"
        dictionary based on the "key= sent_freq.get"

        nlargest() function with key=sent_freq.get is used to retrieve the sentences
        with the highest frequencies from the sent_freq dictionary. The key parameter
        allows us to specify the values (frequencies) associated with each sentence 
        for comparison to determine the largest sentences.
   



## 🚀 About Me

Allow me to introduce Arjun Sherpa, an enthusiastic individual with a passion for ML, Deep Learning, Data Science, and computational neuroscience. Arjun's passion for computational neuroscience reflects their interest in understanding the intricate workings of the brain.

Exploring the intersection of neuroscience and Deep Neural Networks(artificial intelligence), seeking to unlock new insights into cognition and behavior is very much fascinating to me.

I am continuously trying to learn & update myself with new things on this emerging fascinating fields.


reach me: 
Github: https://github.com/settings/admin

linkedIn: https://www.linkedin.com/in/arjun-sherpa-153673198/

gmail: righthuman082@gmail.com
