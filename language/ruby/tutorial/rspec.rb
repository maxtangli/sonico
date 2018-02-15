# http://rspec.info/documentation/3.6/rspec-core/

require 'rspec'

RSpec.describe String do
  it 'treat empty string as true' do
    expect(v = '' ? 1 : 0).to eq(1)
  end
end