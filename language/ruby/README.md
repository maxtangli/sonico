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

core3.7 https://relishapp.com/rspec/rspec-core/v/3-7/docs
~~~~
describe, context, it
shared_examples, include_examples, it_behaves_like, subject
shared_context, include_context

before, after, :suit, :contexnt, :example
around
when_first_matching_example_defined

subject { [1, 2, 3] }, subject(:global_count) { $count += 1 }, it { should be_empty }
let # help method, lazy_evaluated 
described_class, .metadata[:foo]
~~~~

match
~~~~
expect to, not_to, and, or
eq, be >, be_within(delta).of
be, be_a, be_true, be_xxx
match, include, cover
raise_error, yiled
~~~~

# rails

Rails philosophy: DRY, Convention Over Configuration.

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

# view

form_tag
~~~~
<%= form_tag do %>
  Form contents
<% end %>

<form accept-charset="UTF-8" action="/" method="post">
  <input name="utf8" type="hidden" value="&#x2713;" />
  <input name="authenticity_token" type="hidden" value="J7CBxfHalt49OSHp27hblqK20c9PgwJ108nDHX/8Cts=" />
  Form contents
</form>
~~~~

search form
~~~~
<%= form_tag("/search", method: "get") do %>
  <%= label_tag(:q, "Search for:") %>
  <%= text_field_tag(:q) %>
  <%= submit_tag("Search") %>
<% end %>

<form accept-charset="UTF-8" action="/search" method="get">
  <input name="utf8" type="hidden" value="&#x2713;" />
  <label for="q">Search for:</label>
  <input id="q" name="q" type="text" />
  <input name="commit" type="submit" value="Search" />
</form>

# handle multiple hashes in form helper calls
form_tag({controller: "people", action: "search"}, method: "get", class: "nifty_form")
~~~~

model helpers
~~~~
<%= text_field(:person, :name) %>
<input id="person_name" name="person[name]" type="text" value="Henry"/>
~~~~

binding form to object
~~~~
<%= form_for @article, url: {action: "create"}, html: {class: "nifty_form"} do |f| %>
  <%= f.text_field :title %>
  <%= f.text_area :body, size: "60x12" %>
  <%= f.submit "Create" %>
<% end %>

<%= form_for @person, url: {action: "create"} do |person_form| %>
  <%= person_form.text_field :name %>
  <%= fields_for @person.contact_detail do |contact_detail_form| %>
    <%= contact_detail_form.text_field :phone_number %>
  <% end %>
<% end %>

# simple way for resoruces :articles 
form_for(@article)
form_for [:admin, :management, @article]

# simulate patch method
form_tag(search_path, method: "patch")
<form accept-charset="UTF-8" action="/search" method="post">
  <input name="_method" type="hidden" value="patch" />
  <input name="utf8" type="hidden" value="&#x2713;" />
  <input name="authenticity_token" type="hidden" value="f755bb0ed134b76c432144748a6d4b7a7ddf2b71" />
  ...
</form>
~~~~

options
~~~~
<%= select_tag(:city_id, options_for_select([['Lisbon', 1], ['Madrid', 2], ...], 2)) %>

<%= select(:person, :city_id, [['Lisbon', 1], ['Madrid', 2], ...]) %>
<%= f.select(:city_id, ...) %>

<%= options_from_collection_for_select(City.all, :id, :name) %>
<%= collection_select(:person, :city_id, City.all, :id, :name) %>
<%= f.collection_select(:city_id, City.all, :id, :name) %>
~~~~

display model validation errors
~~~~
<% if @article.errors.any? %>
  <div id="error_explanation">
    <h2><%= pluralize(@article.errors.count, "error") %> prohibited this article from being saved:</h2>
 
    <ul>
    <% @article.errors.full_messages.each do |msg| %>
      <li><%= msg %></li>
    <% end %>
    </ul>
  </div>
<% end %>

# generated by form_helpers
<div class="field_with_errors">
 <input id="article_title" name="article[title]" size="30" type="text" value="">
</div>
~~~~

naming convertions
~~~~
<input id="person_name" name="person[name]" type="text" value="Henry"/>
<input id="person_address_city" name="person[address][city]" type="text" value="New York"/>

# array
<input name="person[phone_number][]" type="text"/>
<input name="person[phone_number][]" type="text"/>
<input name="person[phone_number][]" type="text"/>

# array of hash. new a hash when encounter existed key.
<input name="addresses[][line1]" type="text"/>
<input name="addresses[][line2]" type="text"/>
<input name="addresses[][city]" type="text"/>

# complex example
<%= fields_for 'person[address][primary][]', address do |address_form| %>
  <%= address_form.text_field :city %>
<% end %>
<input id="person_address_primary_1_city" name="person[address][primary][1][city]" type="text" value="bologna" />
~~~~

render
~~~~
layout "application" # default
render controller_name.html.erb # default

render inline: "xml.p {'Horrid coding practice!'}", type: :builder # debug only
render plain: "OK"
render html: helpers.tag.strong('Not Found')
render json: @product
render js: "alert('Hello Rails');"

head :created, location: photo_path(@photo)

redirect_to photos_url
redirect_back(fallback_location: root_path)
~~~~

layout
~~~~
auto_discovery_link_tag, javascript_include_tag, stylesheet_link_tag, image_tag, video_tag, audio_tag

_.erb
<html>
  <head>
  <%= yield :head %>
  </head>
  <body>
  <%= yield %>
  </body>
</html>

# usecase: load page-specific js files etc.
.erb
<%= yield %>
<% content_for :head do %>
  <title>A simple page</title>
<% end %>
~~~~

partials
~~~~
# render _menu.html.erb at
<%= render "menu" %>

# explicitly specifying :partial is required when passing additional options
<%= render partial: "link_area", layout: "graybar" %>
<%= render partial: "form", locals: {zone: @zone} %>
<%= render partial: "product", collection: @products, as: :item %>
<%= render partial: @products, spacer_template: "product_ruler" %>

_.erb
<% if local_assigns[:full] %>...
.erb
<%= render article, full: true %>

# collection detect by model name
_.erb
<p>Product Name: <%= product.name %></p>
.erb
<%= render @products %>
~~~~

# controller

params send
- GET /clients?ids[]=1&ids[]=2&ids[]=3
- name="client[address][postcode]"
- Content-Type: application/json. to safely omit root element, set config.wrap_parameters=true or call wrap_parameters in controller.

params access
- default_url_options
- controller_name, action_name
- params.require(:person).permit(:name, :age).permit(id: []) ActionController::Parameters.action_on_unpermitted_parameters = :raise
- params.require(:log_entry).permit!
- private def person_params

session
- Rails.application.config.session_store :cache_store, key: xx, domain: xx
- session[:current_user_id], session[:current_user_id] = nil, reset_session

cookie
- cookies[:commenter_name]
- Rails.application.config.action_dispatch.cookies_serializer = :json

flash
- values only be available in the next request
- flash[:notice] = "You have successfully logged out.", redirect_to root_url
- redirect_to root_url, notice: "You have successfully logged out."
- redirect_to root_url, flash: { referral_code: 1234 }
- flash.keep; redirect_to users_url
- flash.now[:error] = "Could not save client"

filters
- before_action :require_login
- skip_before_action :require_login, only: [:new, :create]
- around_action :wrap_in_transaction, only: :show
- before_action LoginFilter # def self.before

request object
- url, protocol, host, port, domain, query_string, method, get? ..., headers
- remote_ip
- path_parameters, query_parameters, request_parameters

response object
- not usually used directly
- body, status, headers, location, content_type, charset...
- response.headers["Content-Type"] = "application/pdf"

response
- render json: @users
- send_data
- send_file
- include ActionController::Live

csrf
- from helpers, authenticity_token

https
- force_ssl except: :cheeseburger # config.force_ssl

rescue
- default: 404.html, 500.html
- rescue_from ActiveRecord::RecordNotFound, with: :record_not_found

log filtering
- filter_parameter_logging.rb: Rails.application.config.filter_parameters += [:password]
- config.filter_redirect.concat ['s3.amazonaws.com', /private_path/]

# model

query
- r: return ActiveRecord::Relation or single model. find(10), find([1, 10]), find_by(hash), find_by_field_name_and_locked, find_by_sql, connection.select_all.to_hash, exists?, all, take(n), first(n), last(n)
- r batch(> 10000 records): find_each(batch_size: 1000, start: xx, finish: xx), find_in_batches(...)
- filtering: select(:name), pluck(:id), distinct, limit(5).offset(30), ids
- condition: where(string, array_or_hash), where(hash), not, or, enum availability: [:available, :unavailable]; Book.available
- ordering: order(:created_at), order(created_at: :desc)
- group: select("date(created_at) as ordered_date, sum(price) as total_price").group("date(created_at)").having("sum(price) > ?", 100), group(:status).count/average/minimum/maximum/sum
- join
- overriding conditon: default_scope, merge(scope), unscoped, unscope(:order), unscope(where: :id), only(:order, :where), reorder('name'), reverse_order, rewhere, none
- lock: readonly, default optimistic locking, .lock
- eager loading: Client.includes(:address).limit(10)

operation
- c: create, find_or_create_by(hash), find_or_initialize_by(hash)
- u: user.save, user.update(hash), User.update_all("field=xx")
- d: user.destroy, User.where(hash).destroy_all

validate
- helpers: acceptance, validates_associated, confirmation, exclusion, format, inclusion, length, numericality, presence, uniqueness, validates_with, validates_each.
- common options: :allow_nil, :allow_blank, :message, :on, :strict, :if
- trigger: create, save, update
- errors, errors.details

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