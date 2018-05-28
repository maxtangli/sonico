require 'csv_parser'

RSpec.describe CsvParser do
  shared_examples '#read_csv' do |filename|
    it 'read csv content exactly' do
      file   = File.expand_path("fixtures/files/#{filename}", __dir__)
      result = CsvParser.read_csv(file)
      expect(result).to eq([['a', 'あ'], ['b', 'び']])
    end
  end

  describe '#read_csv' do
    context 'utf8' do
      it_behaves_like '#read_csv', 'utf8.csv'
    end

    context 'utf8bom' do
      it_behaves_like '#read_csv', 'utf8bom.csv'
    end

    context 'excel outputed' do
      it_behaves_like '#read_csv', 'excel_sjis_extra-line.csv'
    end

    context 'utf8 lf' do
      it_behaves_like '#read_csv', 'utf8_lf.csv'
    end
  end
end
