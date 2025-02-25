from abc import ABC, abstractmethod

# Abstract Class
class DataMiner(ABC):
    def mine_data(self, path: str) -> None:
        # Template method
        file = self.open_file(path)
        data = self.extract_data(file)
        analysis = self.parse_data(data)
        self.send_report(analysis)
        self.close_file(file)

    @abstractmethod
    def open_file(self, path: str) -> any:
        pass

    @abstractmethod
    def extract_data(self, file: any) -> list:
        pass

    @abstractmethod
    def parse_data(self, data: list) -> str:
        pass

    def send_report(self, analysis: str) -> None:
        print(f"Sending report: {analysis}")

    def close_file(self, file: any) -> None:
        print("Closing file")

# Concrete Classes
class PDFDataMiner(DataMiner):
    def open_file(self, path: str) -> any:
        print(f"Opening PDF file: {path}")
        return f"PDF_FILE_{path}"

    def extract_data(self, file: any) -> list:
        print(f"Extracting data from PDF: {file}")
        return ["PDF_DATA_1", "PDF_DATA_2"]

    def parse_data(self, data: list) -> str:
        print(f"Parsing PDF data: {data}")
        return "PDF Analysis Results"

class CSVDataMiner(DataMiner):
    def open_file(self, path: str) -> any:
        print(f"Opening CSV file: {path}")
        return f"CSV_FILE_{path}"

    def extract_data(self, file: any) -> list:
        print(f"Extracting data from CSV: {file}")
        return ["CSV_DATA_1", "CSV_DATA_2"]

    def parse_data(self, data: list) -> str:
        print(f"Parsing CSV data: {data}")
        return "CSV Analysis Results"

def main():
    # Create miners
    pdf_miner = PDFDataMiner()
    csv_miner = CSVDataMiner()

    # Mine data from different file types
    print("Processing PDF:")
    pdf_miner.mine_data("document.pdf")
    print("\nProcessing CSV:")
    csv_miner.mine_data("data.csv")

if __name__ == "__main__":
    main()