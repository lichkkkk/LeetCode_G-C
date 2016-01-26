class Solution {
public:
	string minWindow(string s, string t) {
		int count[256 * 2] = { 0 };

		int distinct[256 * 2] = { 0 };
		int cnt = 0; // count distint in t
		for (int i = 0; i < t.size(); i++) {
		    unsigned char c = t[i];
			if (distinct[c] == 0)
			{
				cnt++;
			}
			distinct[c]++;
		}

		int appear = 0;
		bool flag = false;
		int front = 0;

		int shortest = s.size();
		int start = 0;
		
		for (int i = 0; i < s.size(); i++) {
		    unsigned char c = s[i];
			// not in t;
			if (distinct[c] == 0) continue;
			
			count[c] ++;
			
			if (count[c] == distinct[c]) {
				appear++;
				if (appear == cnt)
					flag = true;
			}

			while (front <= i && 
			       (count[s[front]] >= distinct[s[front]] + 1 || distinct[s[front]] == 0 ))
			{
				count[s[front]]--;
				front++;
			}

			if (flag && i - front + 1 < shortest) {
				start = front;
				shortest = i - front + 1;
			}

		}

		if (!flag) return string("");

		return string(s.begin() + start, s.begin() + start + shortest);


	}
};
