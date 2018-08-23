import requests
from bs4 import BeautifulSoup
from datetime import date, datetime
from decimal import Decimal

class Agespisa(object):
	"""
	Class that represents the shares of the matriculation and the client linked to agespisa.
	"""
	def __init__(self, register_id):
		self.register_id = register_id
		request_one = requests.get("http://www.agespisa.com.br/exibirEmitirSegundaViaContaInternetAcessoGeralAction.do?acessoGeral=sim")
		if request_one.status_code != 200:
			raise Exception('Connection not established to www.agespisa.com.br ...')
		
		soup = BeautifulSoup(request_one.content, 'html.parser')
		tag = soup.find('form', {'name':'EmitirSegundaViaContaInternetActionForm'})
		end_tag = tag['action']
		final_string = 'http://www.agespisa.com.br'+end_tag

		self.request = requests.post(final_string, data = {'matricula':self.register_id})
		if self.request.status_code != 200:
			raise Exception('Connection not established to www.agespisa.com.br ...')

		new_soup = BeautifulSoup(self.request.content, 'html.parser')
		self.register = new_soup.find('input', {'name':'matricula'})['value']
		self.name = new_soup.find('input', {'name':'nomeCliente'})['value']
		self.city = new_soup.find('input', {'name':'elo'})['value']
		self.debit_amount = Decimal(new_soup.find('input', {'name':'valorDebito'})['value'].replace('.','').replace(',','.'))
		self.date_debit_amount = datetime.strptime(new_soup.find('input', {'name':'dataDebito'})['value'], '%d/%m/%Y').date()
		self.addition = Decimal(new_soup.find('input', {'name':'debitoACobrar'})['value'].replace('.','').replace(',','.'))

		self.debits = self.__water_bills_function(new_soup)

	def __repr__(self):
		return "<register_id: {}, name: {}, debit_amount: {}>".format(
				self.register, self.name, self.debit_amount)

	def __water_bills_function(self, new_soup):
		debits = new_soup.find_all('tr', {'bgcolor':'#FFFFFF'})
		chars = ['0','1','2','3','4','5','6','7','8','9',',','/']
		list_bill_final = list()
		for debit_html in debits:
			select = debit_html.find_all('div', {'align':'center'})
			
			# get month			
			list_final_month = list()
			for char in select[0].text:
				if char in chars: 
					list_final_month.append(char)
			value_month_str = "".join(list_final_month)
			format_value_month_str = date(day=1,month=int(value_month_str.split("/")[0]), year=int(value_month_str.split("/")[1]))

			# get value
			list_final_value = list()
			for char in select[1].text:
				if char in chars: 
					list_final_value.append(char)
			value_value_str = "".join(list_final_value)
			format_value_value_str = Decimal(value_value_str.replace('.','').replace(',','.'))

			bill_link_html = debit_html.find_all('td', {'width':'15%'})[1]
			t = bill_link_html.find('a')
			value_link = 'www.agespisa.com.br/gsan/gerarRelatorio2ViaContaAction.do?cobrarTaxaEmissaoConta=N&idConta' + t['href'].split('+')[1].split(',')[0]

			list_bill_final.append(self.Debits(format_value_month_str, format_value_value_str, value_link))

		return list_bill_final

	class Debits(object):
		"""
		Class that displays the user's debits.
		"""
		def __init__(self, month, value, link):
			self.month = month
			self.value = value
			self.link = link

		def __repr__(self):
			return "<month: {}, value: {}, link: {}>".format(
				self.month, self.value, self.link)
