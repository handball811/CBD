from Generator.generator import SentenceGenerator


if __name__ == "__main__":
	gen = SentenceGenerator()
	for e in gen.generate("sample"):
		print(e)