//ugly code, do not want to improve
class Solution {
public:
   string addBinary(string a, string b) {
    	string res;
    	string lessDigits, moreDigits;
    	if(a.size() < b.size()){
    		lessDigits = a; 
    		moreDigits = b;
    	}
    	else{
    		lessDigits = b; 
    		moreDigits = a;
    	}
    	//int sz = lessDigits.size();
    	int i = -1;
    	int forwDigit = 0;
    	auto itLess = lessDigits.crbegin(), itMore = moreDigits.crbegin(); 
    	while(itLess < lessDigits.crend()){
            int addRes = *itLess - '0' + 
                         *itMore - '0' + 
                         forwDigit;
            if(addRes == 1) {res.append(1,'1'); forwDigit = 0;} 
            else if(addRes == 2){res.append(1,'0'); forwDigit = 1;}
            else if(addRes == 3){res.append(1,'1'); forwDigit = 1;}
            else res.append(1,'0');
            ++itLess;
            ++itMore;
            //cout<<res<<endl;
    	}
    	while(itMore < moreDigits.crend()){
    		int addRes = *itMore - '0' + 
                         forwDigit;
            if(addRes == 1) {res.append(1,'1'); forwDigit = 0;} 
            else if(addRes == 2){res.append(1,'0'); forwDigit = 1;}
            else if(addRes == 3){res.append(1,'1'); forwDigit = 1;}
            else res.append(1,'0');
            ++itMore;
            //cout<<res<<"  addRes " <<addRes << endl;
    	}
        if(forwDigit == 1) res.append(1,'1');
        return string(res.crbegin(), res.crend());

    }
};
