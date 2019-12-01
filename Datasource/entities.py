from dataclasses import dataclass

@dataclass
class DataInformation:
	# 暗号化の際に使われた情報
	rot_num :int


@dataclass
class Encrypted:
	# 暗号化されたデータに関する情報
	sentence :str
	info     :DataInformation

@dataclass
class Decypted:
	# 復号化されたデータの情報
	sentence :str

