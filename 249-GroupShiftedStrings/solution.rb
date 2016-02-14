# @param {String[]} strings
# @return {String[][]}
#
# 249. Group Shifted Strings
# Tag: Hash
#   MY FIRST Ruby SOLUTION
# Chang Li at UC San Diego
# Feb. 13, 2016

def group_strings(strings)
    map = Hash.new([])
    for string in strings
        pattern = get_pattern(string)
		map[pattern] += [string]
    end
    res = []
    map.each_key{|key| res += [map[key].sort]}
    return res.sort
end

def get_pattern(string)
    diff = string[0].ord - 'a'.ord
    pattern = ""
    string.each_char{ |c| pattern << (((c.ord-97)+26-diff)%26+97).chr}
	return pattern
end
