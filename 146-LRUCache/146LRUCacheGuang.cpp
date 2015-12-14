
class LRUCache {
	struct DoubleLinkedNode {
		int key, val;
		DoubleLinkedNode *pre, *next;
		DoubleLinkedNode(int _key, int _val, DoubleLinkedNode * _pre = NULL, DoubleLinkedNode *  _next = NULL) {
			key = _key;
			val = _val;
			pre = _pre;
			next = _next;
		}
	};

private:
	unordered_map<int, DoubleLinkedNode *> m;
	int cnt = 0;
	int cap = 0;
	DoubleLinkedNode * head = NULL;
	DoubleLinkedNode * tail = NULL;

	void update(DoubleLinkedNode * p) {
		if (p == NULL) return;
		if (head == p) return;
		auto t = p;
		p->pre->next = p->next;
		if(p->next) p->next->pre = p->pre;
		
		if (tail == p) {
            tail = p->pre;
		}
        p->pre = NULL;
        head->pre = p;
        p->next = head;
        head = p;
	}

	void insert(int key, int value) {
		if (cnt >= cap) return;
		auto p = new DoubleLinkedNode(key, value);
        p->next = head;
        if(head) head->pre = p;
        else tail = p;
        head = p;
		//m.insert(make_pair<int, DoubleLinkedNode*>(key, p));
		m[key] = p;
		++cnt;
	}

	void deleteTail() {
		if (tail) {
		    m.erase(tail->key);
			auto p = tail;
			tail = tail->pre;
			if (tail) tail->next = NULL;
			else head = NULL;
			delete p;
			--cnt;
		}
	}
public:
	LRUCache(int capacity) {
		cap = capacity;
		cnt = 0;
		head = NULL;
		tail = NULL;
	}

	int get(int key) {
		auto p = m.find(key);
		if (p != m.end()) {
			update(p->second);
			return p->second->val;
		}
		return -1;
	}

	void set(int key, int value) {
		auto p = m.find(key);
		if (p != m.end()) {
			//already exists, just update
			p->second->val = value;
			update(p->second);
		}
		else {
			if (cnt <= cap - 1) {
				// insert to tail
				insert(key, value);
			}
			else {
				// delete tail and insert to tail
				deleteTail();
				insert(key, value);
			}
		}
	}
};
