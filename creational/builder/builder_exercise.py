import abc
from io import StringIO
from typing import List
import csv

from black import Report

file_content = '''
Jan Kowalski M 45
Anna Nowak F 23
Zenon Nijaki M 33
Ewa Nowakowska F 19
'''.strip()

class ReportBuilder(abc.ABC):
    @abc.abstractmethod
    def add_header(self, header: str):
        pass

    @abc.abstractmethod
    def begin_data(self):
        pass

    @abc.abstractmethod
    def end_data(self):
        pass

    @abc.abstractmethod
    def add_row(self, row: List[str]):
        pass

    @abc.abstractmethod
    def add_footer(self, footer):
        pass

    @abc.abstractmethod
    def get_report(self):
        pass


class HTMLBuilder(ReportBuilder):
    def __init__(self):
        self._report_parts = []

    def add_header(self, header):
        self._report_parts.append(f"<h1>{header}</h1>")
        return self

    def begin_data(self):
        self._report_parts.append("<table>")
        return self

    def end_data(self):
        self._report_parts.append("</table>")
        return self

    def add_row(self, row: List[str]):
        parts = list()
        parts.append("<tr>")
        [parts.append(f"<td>{word}</td>") for word in row]
        parts.append("</tr>")

        self._report_parts.extend(parts)
        return self

    def add_footer(self, footer):
        self._report_parts.append(f'<div class="footer">{footer}</div>   ')
        return self

    def get_report(self):
        return '\n'.join(self._report_parts)


class CSVBuilder(ReportBuilder):
    def __init__(self):
        self._stream = StringIO()
        self._csv_writer = csv.writer(self._stream)

    def add_header(self, header: str):
        pass

    def add_footer(self, footer):
        return super().add_footer(footer)

    def begin_data(self):
        pass

    def end_data(self):
        pass
        
    def add_row(self, row):
        self._csv_writer.writerow(row)
        return self
        
    def get_report(self):
        self._stream.seek(0)
        return self._stream.read()

class DataParser:
    def __init__(self, builder: ReportBuilder):
        self._builder  = builder

    def parse(self, stream):
        self._builder.add_header('Report')
        self._builder.begin_data()
        for line in stream:
            line = line.strip()
            if not line:
                continue
            data = line.split()
            self._builder.add_row(data)
        self._builder.end_data()
        self._builder.add_footer('Copyright 2022')


def main(report_builder, stream):
    parser = DataParser(report_builder)
    parser.parse(stream)
    doc = report_builder.get_report()
    print(doc)


if __name__ == "__main__":
    main(HTMLBuilder(), StringIO(file_content))

    # <h1>Report</h1>
    # <table>
    #   <tr>
    #     <td>Jan</td>
    #     <td>Kowalski</td>
    #     <td>M</td>
    #     <td>45</td>
    #   </tr>
    #   <tr>
    #     <td>Anna</td>
    #     <td>Nowak</td>
    #     <td>F</td>
    #     <td>23</td>
    #   </tr>
    #   <tr>
    #     <td>Zenon</td>
    #     <td>Nijaki</td>
    #     <td>M</td>
    #     <td>33</td>
    #   </tr>
    #   <tr>
    #     <td>Ewa</td>
    #     <td>Nowakowska</td>
    #     <td>F</td>
    #     <td>19</td>
    # ...
    #   </tr>
    # </table>
    # <div class="footer">End of report</div>   
     
    #############################################################

    main(CSVBuilder(), StringIO(file_content))

    # Jan,Kowalski,M,45
    # Anna,Nowak,F,23
    # Zenon,Nijaki,M,33
    # Ewa,Nowakowska,F,19

    ############################################################

    doc = HTMLBuilder() \
            .add_header('footer') \
            .begin_data() \
                .add_row(['one', 'two', 3]) \
                .add_row(['four', 'five', 6]) \
            .end_data() \
            .add_footer('footer') \
            .get_report() 

    print(doc)

    # <h1>footer</h1>
    # <table>
    #   <tr>
    #     <td>one</td>
    #     <td>two</td>
    #     <td>3</td>
    #   </tr>
    #   <tr>
    #     <td>four</td>
    #     <td>five</td>
    #     <td>6</td>
    #   </tr>
    # </table>
    # <div class="footer">footer</div>


