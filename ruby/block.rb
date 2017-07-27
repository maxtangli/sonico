def hello_block
  yield("hello") if block_given?
end

# in ruby, use block as a callback
hello_block {|s| puts s}