# setup

rbenv
~~~~
# setup rbenv
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
cd ~/.rbenv && src/configure && make -C src
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
~/.rbenv/bin/rbenv init
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
exec $SHELL -l

# setup rbenv-install
mkdir -p "$(rbenv root)"/plugins
git clone https://github.com/rbenv/ruby-build.git "$(rbenv root)"/plugins/ruby-build
rbenv install --list

# install rbenv ruby via rbenv-install
sudo yum install -y openssl-devel readline-devel zlib-devel
rbenv install 2.5.1
rbenv global 2.5.1
rbenv version

# validate via rbenv-doctor script
curl -fsSL https://github.com/rbenv/rbenv-installer/raw/master/bin/rbenv-doctor | bash
exec $SHELL -l
ruby -v

# install bundle
gem install bundle
echo 'alias be="bundle exec "' >> ~/.bashrc

# install sqlite3
sudo yum install -y sqlite-devel

# install javascript runtime
sudo yum install -y nodejs

# install nokogiri
# vagrant box update
sudo yum install -y gcc ruby-devel zlib-devel

# new rails project
gem install rails
rails new example
cd example
rails s
# Yay! You’re on Rails!
~~~~

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
	load # for dev. read file everytime
	require # common use. read file once and cache in memory
	require_relative # rarely used since gems located in $LOAD_PATH.
	autoload(module, filename) # call require when first accessed
	global_variables, __dir__
	__method__, __callee__, caller_xx, block_given?, iterator?	
	
	# syscall
	binding, eval 
	`cmd`, fork, exec, spawn, select, syscall, system, test
	sleep, abort([msg]), exit, at_exit { block }, set_trace_func	
end

.rb .o .so .dll
ruby -e 'puts $LOAD_PATH'
/home/vagrant/.rbenv/rbenv.d/exec/gem-rehash
/home/vagrant/.rbenv/versions/2.5.1/lib/ruby/gems/2.5.0/gems/did_you_mean-1.2.0/lib
/home/vagrant/.rbenv/versions/2.5.1/lib/ruby/site_ruby/2.5.0
/home/vagrant/.rbenv/versions/2.5.1/lib/ruby/site_ruby/2.5.0/x86_64-linux
/home/vagrant/.rbenv/versions/2.5.1/lib/ruby/site_ruby
/home/vagrant/.rbenv/versions/2.5.1/lib/ruby/vendor_ruby/2.5.0
/home/vagrant/.rbenv/versions/2.5.1/lib/ruby/vendor_ruby/2.5.0/x86_64-linux
/home/vagrant/.rbenv/versions/2.5.1/lib/ruby/vendor_ruby
/home/vagrant/.rbenv/versions/2.5.1/lib/ruby/2.5.0
/home/vagrant/.rbenv/versions/2.5.1/lib/ruby/2.5.0/x86_64-linux

C:/Ruby25-x64/lib/ruby/site_ruby/2.5.0
C:/Ruby25-x64/lib/ruby/site_ruby/2.5.0/x64-msvcrt
C:/Ruby25-x64/lib/ruby/site_ruby
C:/Ruby25-x64/lib/ruby/vendor_ruby/2.5.0
C:/Ruby25-x64/lib/ruby/vendor_ruby/2.5.0/x64-msvcrt
C:/Ruby25-x64/lib/ruby/vendor_ruby
C:/Ruby25-x64/lib/ruby/2.5.0
C:/Ruby25-x64/lib/ruby/2.5.0/x64-mingw32
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

lambda
- block: not object. call by yield.
- proc: do not check number of arguments, abort execution after .call
- lambda: {}, ->() {}, a special Proc that check number of arguments, keep execution after .call, support curry

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

# use case

stdlib
~~~~
Forwardable, Observable, Singleton etc.
~~~~

assert
- raise unless

interface
- way1: duck typing + tdd
- way2: module def method raise -> include module

immutable
- constructor call freeze

singleton
- include Singleton

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

# config/routes.rb

action convention
- index
- new, show, edit
- create, update, destroy

resourceful routes
- resources :atricles
- get 'profile', to: 'users#show'
- adding member/collection routes

reuse
- concern
- naming: get 'exit', to: 'sessions#destroy', as: :logout
- wildcard segments: get 'photos/*other', to: 'photos#unknown'

nesting
- namespace :admin do
- nested resources: suggest at most 1 level deep. http://weblog.jamisbuck.org/2007/2/5/nesting-resources
- shallow nesting

non-resourceful routes
- bound routes: get 'photos(/:id)', to: :display
- dynamic segments: get 'photos/:id/:user_id', to: 'photos#show'
- static segments: get 'photos/:id/with_user/:user_id', to: 'photos#show'
- defaults: get 'photos/:id', to: 'photos#show', defaults: { format: 'jpg' }
- verb constranints: match 'photos', to: 'photos#show', via: [:post, :delete]
- segment constranints: get 'photos/:id', to: 'photos#show', id: /[A-Z]\d{5}/
- request-based constranints: get 'photos', to: 'photos#index', constraints: { subdomain: 'admin' }

etc
- redirect: get '/stories/:name', to: redirect('/articles/%{name}')
- root 'pages#main'
- get 'こんにちは', to: 'welcome#index'
- direct :homepage do
- resolve("Basket") { [:basket] }

>rails routes # http://localhost:3000/rails/info/routes
~~~~
       Prefix Verb   URI Pattern                  Controller#Action
     articles GET    /articles(.:format)          articles#index
              POST   /articles(.:format)          articles#create
  new_article GET    /articles/new(.:format)      articles#new
 edit_article GET    /articles/:id/edit(.:format) articles#edit
      article GET    /articles/:id(.:format)      articles#show
              PATCH  /articles/:id(.:format)      articles#update
              PUT    /articles/:id(.:format)      articles#update
              DELETE /articles/:id(.:format)      articles#destroy
~~~~

url helpers
- edit_article_path(:id), edit_article_url(:id)
- magazine_ad_path(@magazine, @ad), url_for([@magazine, @ad]), [@magazine, @ad], [:edit, @magazine, @ad]

# autoloading

ruby const resolution
- relative const resolution: nesting -> ancestor -> Object -> const_missing
- qualified const resolution: relative::qualified.
- parent namespace

rails
- autoload_paths: app/*, app/*/concern, test/mailers/previews
- eager_load_paths: app/*, app/*/concern
- const resolution: iterate autoload_paths
- to support lazy, Module#autoload not used

rails dev
- eager_load=false, cache_classes=false.

rails test
- eager_load=false

rails release
- eager_load=true, config.cache_classes=true.

bin/rails r 'puts ActiveSupport::Dependencies.autoload_paths'
~~~~
/vagrant/reisen/app/assets
/vagrant/reisen/app/channels
/vagrant/reisen/app/controllers
/vagrant/reisen/app/controllers/concerns
/vagrant/reisen/app/helpers
/vagrant/reisen/app/jobs
/vagrant/reisen/app/mailers
/vagrant/reisen/app/models
/vagrant/reisen/app/models/concerns
/home/vagrant/.rbenv/versions/2.5.1/lib/ruby/gems/2.5.0/gems/activestorage-5.2.0/app/assets
/home/vagrant/.rbenv/versions/2.5.1/lib/ruby/gems/2.5.0/gems/activestorage-5.2.0/app/controllers
/home/vagrant/.rbenv/versions/2.5.1/lib/ruby/gems/2.5.0/gems/activestorage-5.2.0/app/controllers/concerns
/home/vagrant/.rbenv/versions/2.5.1/lib/ruby/gems/2.5.0/gems/activestorage-5.2.0/app/javascript
/home/vagrant/.rbenv/versions/2.5.1/lib/ruby/gems/2.5.0/gems/activestorage-5.2.0/app/jobs
/home/vagrant/.rbenv/versions/2.5.1/lib/ruby/gems/2.5.0/gems/activestorage-5.2.0/app/models
/vagrant/reisen/test/mailers/previews
~~~~