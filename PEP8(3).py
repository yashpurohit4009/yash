def test_pep8(self):
        """ runner """
        arglist = [['statistics', True],
                   ['show-source', True],
                   ['repeat', True],
                   ['paths', [BASE_DIR]]]

        pep8style = pep8.StyleGuide(arglist,
                                    parse_argv=False,
                                    config_file=True)
        options = pep8style.options
        report = pep8style.check_files()
        if options.statistics:
            report.print_statistics()

        # reporting errors (additional summary)
        errors = report.get_count('E')
        warnings = report.get_count('W')
        message = 'pep8: %d errors / %d warnings' % (errors, warnings)
        print(message)
        assert report.total_errors == 0, message 
