class Solution {
public:
    bool isPalindrome(string s) {
         vector<char>vic;
        for(int i=0;i<s.size();i++){
            if(s[i]>='a'&&s[i]<='z'||s[i]>='A'&&s[i]<='Z'||s[i]>='0'&&s[i]<='9'){
                if(s[i]>='A'&&s[i]<='Z'){
                    s[i]=tolower(s[i]);
                }
                vic.push_back(s[i]);
            }
        }
       
        for(int i=0;i<vic.size()/2;i++){
            if(vic[i]!=vic[vic.size()-1-i]){
                return false;
            }
        }
        return true;
        
    }
};