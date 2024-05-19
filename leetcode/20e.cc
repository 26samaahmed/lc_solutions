class Solution {
public:
    bool isValid(string s) {
      std::stack<char> brackets;
      // loop through the string, if a opening bracket is found, push to stack
      // if an ending bracket matches the top of the stack or the last unclosed bracket then pop from stack
      for (auto letter: s) {
          if (letter == '{' || letter == '[' || letter == '(') {
              brackets.push(letter);
          } else if (letter == ')' || letter == ']' || letter == '}') {
              // if the letter is a closing bracket, check if the stack is empty because if it is, then we have
              // an closing with no opening so we should return false right away
              if (brackets.empty()) return false;
              else {
                  if ((brackets.top() == '(' && letter == ')') || 
                  (brackets.top() == '{' && letter == '}') || 
                  (brackets.top() == '[' && letter == ']')) {
                  brackets.pop();
                  } else {
                    return false;
                }
              }
            }
      }
      return brackets.empty();
    }
};
