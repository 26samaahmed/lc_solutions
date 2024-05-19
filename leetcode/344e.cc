class Solution {
public:
    void reverseString(vector<char>& s) {
        // creating a variable that starts from the last letter and i will decrement as i go through the loop
        int end = s.size() - 1;
        // i will start looping from the first index
        for (int begin = 0; begin < end; begin++ ) {
            // we want to store a copy of the original beinning index before it gets modified
            char copy_begin = s[begin];
            // now we change the value at the starting index to the value of the ending inde (switching them)
            s[begin] = s[end]; // now the begin and end have the same value so we need to replace the end value with the original value at the beginning
            s[end] = copy_begin;
            // decrement the end index so we go to the characters prior to the last character
            end--;
        }
        
    }

// input: a vectof of chars
// output: the reversed vector in place
/* thought process: i should start by creating a variable that points at the end of the vector. Then
I will start looping from the beginning until the the value i started with is less than the end value. As i
go through each index, I will replace characters one by one. So i would start by creating a cop  variable that holds the value at the original starting index. Then i change the value at the original starting index with the
value at the end index. Then i will change the value at the ending index using the copy variable of the original value that was stored at the starting index before it was modified.
*/
};
