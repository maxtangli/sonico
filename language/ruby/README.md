# Core 2.4.3

http://ruby-doc.org/core-2.4.3/Kernel.html
~~~~
module Kernel
	# constructor wrapper
	Array etc.
	
	# grammar
	lambda { |...| block } # Proc.new
	loop { block }
	raise(exception [, string [, array]])
	catch([tag]) {|tag| block }
	throw(tag [, obj])
	
	# io
	sprintf # %[flags][width][.precision]type
	gets, readline, readlines # e.g. print while gets
	puts, putc
	print, printf # print obj.to_s
	p # print obj.inspect + "\n"
	warn
	
	# tools
	srand(number = Random.new_seed)
	rand(max=0)
	
	# context
	require, require_relative
	autoload(module, filename), load
	global_variables, __dir__
	__method__, __callee__, caller_xx, block_given?, iterator?	
	
	# syscall
	binding, eval 
	`cmd`, fork, exec, spawn, select, syscall, system, test
	sleep, abort([msg]), exit, at_exit { block }, set_trace_func	
end
~~~~

http://ruby-doc.org/core-2.4.3/Object.html
http://ruby-doc.org/core-2.4.3/Array.html
~~~~
class BasicObject # explicit blank class, used for create object hierarchies, Delegator class etc.

class Object
	include Kernel
	
	ARGV,ARGF,DATA
	ENV,RUBY_XXX
	TOPLEVEL_BINDING #Binding,binding(),eval('@member', aBinding)
	STDIN,STDOUT,STDERR
	
	# 1.compare
	<=> # default ==. used by Enumerable#sort etc. include mixin Comparable to gain <= , ==, between? etc.
	=== # default ==. used by case.
	== # default same object, typically override.

	object_id
	equal? # same object. no override.

	hash # used by Hash.
	eql? # same hash key. typically override by call ==. used by Hash.

	=~ # pattern match, override by Regexp, String etc.

	# 2.convert
	freeze, frozen?
	taint, untaint, tainted? # to prevent insecure data by restricting various built-in methods.

	clone(freeze: true) # shallow copy, tpically with internal state. may have class-specific behavior by initialize_copy().
	dup # shallow copy, typically via new. may have class-specific behavior by initialize_copy().

	to_s # default　class + object_id
	display(port=$>)
	inspect
	tap{|x|...} # debug chain e.g. .tap {|x| puts "original: #{x.inspect}"}

	to_enum(method = :each, *args){|*args| block}

	# 3.meta
	class
	instance_xxx?, nil? ...
	respond_to?(SymbolOrString, include_all=false), respond_to_missing?
	public_send(SymbolOrString [, args...]), send
	extend(module, ...)

	singleton_class
	define_singleton_method(symbol) { block } # ? to impl Singleton patternm, include Singleton
end
~~~~

http://ruby-doc.org/core-2.4.3/Enumerable.html
~~~~
# to mixin, provide #each
# to mixin #max, #min, #sort, provide obj.<=>
module Enumerable
	# description
	include?, one?, any?, all?, none?
	count
	
	# transform
	sort, sort_by, uniq
	each_entry, each_with_index, each_with_object, reverse_each
	each_slice, each_cons
	cycle
	map, flat_map, to_a, to_h, zip
	
	# divide
	partition
	chunk, chunk_while
	group_by
	slice_before, slice_after, slice_when
	
	# filter
	reduce, sum
	find, find_index, find_all
	grep, grep_v
	max, max_by, min, min_by, minmax, minmax_by
	select, reject
	first, take, take_while, drop, drop_while
	
	# advanced
	lazy
end

# created by Kernel#to_enum, ::new etc.
class Enumerator	
end

class Array
	# retrieve
	empty?, [], at, fetch, values_at, last, dig
	bsearch, index, rindex
	sample
	
	# modify
	insert, push <<, pop, unshift, fill
	delete_at, shift, clear
	slice, compact, flatten!, keep_if, delete_if, replace, rreplace
	reverse, rotate, shuffle
	
	# transform
	reverse_each
	permutation, repeated_permutation, combination, repeated_combination
	to_ary, try_convert, *, join
	
	# multiple array
	&, |, concat +, -, product
	assoc, rassoc
	
	# advanced
	pack, transpose
end

# support objects with <=>
class Range
end

class Hash
end

class String
	%, *, +, << concat
	
	codepoints
	count([other_str]+)
	upto
	
	center, ljust, rjust
	dump
end

class Struct
end
~~~~

# grammar

http://ruby-doc.org/core-2.4.3/doc/syntax/control_expressions_rdoc.html
http://ruby-doc.org/core-2.4.3/doc/syntax/literals_rdoc.html
~~~~
# control
if, unless, case
while, until, for in
redo, next, break
upto
rescue, ensure

# methods
my_method(positional1, keyword1: value1, keyword2: value2)

def my_method yield self end

# singleton class
class C
  class << self
    # ...
  end
end

# percent strings
%s %i %I
% %q %Q %w %W
%r
%x
~~~~

# stdlib

~~~~
Forwardable, Observable, Singleton etc.
~~~~

# rails

Rails philosophy: DRY, Convention Over Configuration.

link_to
- 

rotues
- index
- new, show, edit
- create, update, destroy

params
- ActionController::Parameters.action_on_unpermitted_parameters = :raise
- params.require(:person).permit(:name, :age)
