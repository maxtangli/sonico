# https://ruby-doc.org/core-2.4.1/Enumerable.html
# https://ruby-doc.org/core-2.4.1/String.html

class YomeList
  include Enumerable

  def initialize(names)
    @names = names
    yield(self) if block_given?
  end

  def each
    @names.each {|name| yield(name)}
  end
end

memories = YomeList.new(%w{nanoha reisen sonico})
memories = memories.to_enum(:each)

# get: detect=find, find_index, find_all, grep, grep_v, select, reject
# count, include?, all?, any?, one?, none?
# min, max, minmax, min_by, max_by, minmax_by
puts memories.detect {|yome| yome.split(//).rotate(1).join.slice(-3..-1)=='cos'}=='sonico'
puts memories.all? {|yome| yome.include?('n') && yome.length==6}
puts memories.any? {|yome| yome.match?(/([^aeiou][aeiou])+/)}
puts memories.count == memories.count('nanoha') + memories.count {|yome| yome.include?('i')}

# iterate: cycle, each_with_index, each_with_object, reverse_each
# todo: each_cons, each_entry, each_slice, entries
memories.cycle(3) {|yome| print("#{yome} -> ")}

# transform: collect=map, collect_concat, inject=reduce, sort, sort_by, unique, to_a, to_h, zip
# first, take, take_while
# todo: chunk, chunk_while, group_by, partition, flat_map, slice_after, slice_before, slice_when
puts memories.collect {|yome| "dear #{yome}!"}.join(' ')
puts memories.collect_concat {|yome| ["dear #{yome}!", 'moe!']}.join(' ')

# special: lazy

# summary: dispels the silence in the summer boredom.