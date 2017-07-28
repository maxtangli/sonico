# https://ruby-doc.org/core-2.4.1/Enumerable.html
# https://ruby-doc.org/core-2.4.1/String.html

class YomeList
  include Enumerable

  def initialize(names)
    @names = names
  end

  def each
    @names.each {|name| yield(name)}
  end
end

memories = YomeList.new(%w{nanoha reisen sonico})

# get: detect=find, find_index, find_all, all? any?, count
puts memories.detect {|yome| yome.split(//).rotate(1).join.slice(-3..-1)=='cos'}=='sonico'
puts memories.all? {|yome| yome.include?('n') && yome.length==6}
puts memories.any? {|yome| yome.match?(/([^aeiou][aeiou])+/)}
puts memories.count == memories.count('nanoha') + memories.count {|yome| yome.include?('i')}

# iterate: cycle
# todo: each_cons, each_entry, each_slice, each_with_index, each_with_object, entries
memories.cycle(3) {|yome| print("#{yome} -> ")}

# transform: collect=map, collect_concat
# todo: chunk, chunk_while
puts memories.collect {|yome| "dear #{yome}!"}.join(' ')
puts memories.collect_concat {|yome| ["dear #{yome}!", 'moe!']}.join(' ')

# summary: dispels the silence in the summer boredom.