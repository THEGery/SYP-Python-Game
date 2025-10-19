Python Style Guide \- PEP 8

* **Code indentation**  
  * **Tab is allowed** (especially when the code was started with tabs, but 4 spaces are preferred)  
  * **Mixing tabs and spaces is not allowed\!**  
* **Long line alignment options**  
  * a) **using parentheses**: If the first line has arguments (in case of functions) the second line should start exactly aligned to the first parentheses.  
  * b) **Hanging indents**: The first line should not have any arguments, only the opening parentheses.  
* **Multiline constructs (e.g.: lists):**  
  * a) The **closing parentheses/bracket/brace** should line up with the **first non whitespace character**.  
  * b) Or it lines up with the first character that starts the multiline construct.  
  * **But stay consistent\!**  
* **Max line length**  
  * Limit **all line** lengths to max **79** characters.  
  * **Docstrings** and **comments** should be limited to **72** characters  
  * Use **parentheses/brackets/braces** for linebreaks **instead of backslash**.  
    *"The preferred way of wrapping long lines is by using Python’s implied line continuation inside parentheses, brackets and braces. Long lines can be broken over multiple lines by wrapping expressions in parentheses." \- from PEP 8*  
* **Binary operators**  
  * The **operators** should be **on the new line** in front of the operands.  
  * (The operators should be aligned to the opening parentheses in the first line.)  
* **Blank lines**  
  * **Top-level functions** and **class definitions are surrounded** with **two blank lines.**  
  * **Method definitions** **inside a class** are surrounded with a **single blank line**.  
  * **Blank lines** may be used (sparingly) to **separate groups of related functions**.  
  * **Blank lines** can be used (sparingly) **inside functions, to indicate logical sections**.  
* **Source file encoding**  
  * Use **UTF-8**  
  * **avoid non ASCII characters** whenever possible, use them sparingly to name mostly places and human names.  
* **Imports**  
  * **Imports** should be **on separate lines**.  
  * It's ok to have multiple imports on one line in cases like this:  
    **from** math **import** pi, sqrt  
  * *"Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.*

    *Imports should be grouped in the following order:*

    *1\. Standard library imports.*  
    *2\. Related third party imports.*  
    *3\. Local application/library specific imports.*

    *You should put a blank line between each group of imports." \- from PEP 8*

  * Absolute imports are recommended:  
    **import** math,  
     **from** math **import** pi  
  * "Wildcard" imports should be avoided:  
    **from** \<module\> **import** \*  
* **String quotes**  
  * Be consistent  
  * For **docstrings** use **double quotes.**  
* **Whitespace in Expressions and Statements**  
  * [Whitespace in expressions and statements](https://peps.python.org/pep-0008/#whitespace-in-expressions-and-statements)  
  * No trailing whitespaces.  
  * Other recommendations: [PEP 8 – other recommendations](https://peps.python.org/pep-0008/#other-recommendations)  
* **Comments**  
  * **Keep comments up to date\!**  
  * **Comments** should be **complete sentences**, the **first letter** should be **capitalised**.  
  * Comments are easy to understand.  
  * *“Python coders from non-English speaking countries: please write your comments in English, unless you are 120% sure that the code will never be read by people who don’t speak your language.” \- from PEP 8*  
* **Block comments**  
  * Start with \# and **have a space between** the hash and the first letter.  
* **Inline comments**  
  * Use them sparingly.  
    *“An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a \# and a single space.” from PEP 8*  
  * Don’t state the obvious. But sometimes they are useful.  
* **Documentation strings**  
  * Keep all parts of one line doc strings in one line:  
    **“””Docstring text”””**  
  * In case of multiline docstrings, keep the last “”” in a separate line:  
    **“””Docstings with**  
    **multiple lines.**  
    **“””**  
* **Naming conventions**  
  * **Naming style**: [Descriptive naming styles](https://peps.python.org/pep-0008/#descriptive-naming-styles)

  * *“Never use the characters ‘l’ (lowercase letter el), ‘O’ (uppercase letter oh), or ‘I’ (uppercase letter eye) as single character variable names.*  
    *In some fonts, these characters are indistinguishable from the numerals one and zero. When tempted to use ‘l’, use ‘L’ instead.” \- from PEP 8*  
* **Package, module, function names**  
  * **Modules** should have **short names**, all **lower case**. Underscores only when needed for better readability.  
  * **Class names** should normally use the “CapWords” convention  
  * **Function names** should be lower case **with underscores**  
  * **Variable names** same as function names (lower case with underscores)  
* **Constants**  
  * **Constants** are written with **all capital letters** and **underscores.**  
* **Programming Recommendations**  
  * Comparisons to **singletons** *(“In object-oriented programming, the singleton pattern is a software design pattern that restricts the instantiation of a class to a singular instance”)* like **None** should be done with **is**, or **is not.**  
  * Use **is not** rather than **not … is**. E.g.:   
    * **Correct: if** foo **is not** None:  
    * **Wrong:**: if not foo is None:  
  * Always use a **def statement instead** of an **assignment statement that binds a lambda** expression directly to an identifier:  
    * **Correct**: **def** f(x): **return** 2\*x  
    * **Wrong**: f \= **lambda** x: 2\*x  
  * Use ''.startswith() and ''.endswith() instead of string slicing to check for prefixes or suffixes.  
    * **Correct**: **if** foo**.startswith**('bar'):  
    * **Wrong**: **if** foo\[:3\] \== 'bar':  
  * Don’t compare boolean values to True or False using \==:  
    * **Correct**: **if** greetings:  
    * **Wrong**: **if** greeting \== **True**:  
    * **Worse**: **if** greeting is **True**:  
* **Variable annotation**  
  * Annotations for **module level variables**, **class** and **instance variables**, and **local variables** should have a **single space after the colon**.  
  * No space before the colon.  
  * **Equality** “=” should have **one space on both sides**  
    