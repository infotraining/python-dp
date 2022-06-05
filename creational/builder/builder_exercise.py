from io import StringIO

file_content = '''
Jan Kowalski M 45
Anna Nowak F 23
Zenon Nijaki M 33
Ewa Nowakowska F 19
'''.strip()

class HTMLBuilder:
    pass
    # TODO


class CSVBuilder:
    pass
    # TODO

class DataParser:
    pass
    # TODO

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
