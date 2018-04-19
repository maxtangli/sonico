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

# percent strings
%s %i %I
% %q %Q %w %W
%r
%x

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
~~~~

# module

use include to append both class and instance methods
~~~~
module Foo
  def self.included(base)
    base.extend(ClassMethods)
  end
  
  module ClassMethods
    def bar
      puts 'class method'
    end
  end
  
  def foo
    puts 'instance method'
  end
end
~~~~

activesupport::concern

Module#prepend to impl memoizer

# new features

2.5
~~~~
do ... rescue ... end
yiled_self: Unlike tap, it returns the result of the block. see: rails try

About 5-10% performance improvement by removing all trace instructions from overall bytecode.
Block passing by a block parameter (e.g. def foo(&b); bar(&b); end) is about 3 times faster than Ruby 2.4 by “Lazy Proc allocation” technique.
~~~~

2.4

2.3
~~~~
# frozen_string_literal: true
lonely operator &. see: activesupport try!
~~~~

# stdlib

~~~~
Forwardable, Observable, Singleton etc.
~~~~

# rspec

~~~~
expect to, not_to, and, or
eq, be >, be_within(delta).of
be, be_a, be_true, be_xxx
match, include, cover
raise_error, yiled
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

cache
- page(removed from Rails 4.0): default off. 
- action(removed from Rails 4.0): config/environments/ config.action_controller.perform_caching = true if production
- fragment: <% cache_if admin?, product do %><%= render product %><% end %>
- low-level: Rails.cache.fetch
- sql: cache in an action, e.g. Product.all, Product.all. WARN

cache config
- config file: config.cache_store = ...
- ActiveSupport::Cache::DalliStore: High performance memcached client for Ruby.
- cache key: any object is ok.
- bin/rails dev:cache