# -*- coding: utf-8 -*-
import pandas as pd

class TexWriter():

    def __init__(self, *args, **kwargs):
        pass


    def return_list_of_ascending_ints_in_brackets(self,how_many_ints):
        list_of_strings = []
        for w in range(1,how_many_ints+1):
            list_of_strings.append('('+str(w)+')')
        return list_of_strings
    
    def asterisk_creator(self,pvalue):
        if pvalue < 0.01:
            return '***'
        if pvalue <0.05:
            return '**'
        if pvalue <0.1:
            return '*'
        return ''
        
    def return_elements_for_result_table_from_reg(self,reg,title):
        dictionary = {}
        dictionary['     '] = title
        try:
            dictionary['Temperaturet/1000'] = str(reg.params['temp6t410']\
            .round(3))+self.asterisk_creator(reg.pvalues['temp6t410'])
        except:
            dictionary['Temperaturet/1000'] = str(reg.params['avgtemp10']\
            .round(3))+self.asterisk_creator(reg.pvalues['avgtemp10'])
        try:
            dictionary[' '] = '['+str(reg.std_errors['temp6t410']\
                       .round(3))+']'
        except:
            dictionary[' '] = '['+str(reg.std_errors['avgtemp10']\
                       .round(3))+']' 
        try:
            dictionary['Temperaturet-1/1000'] = str(reg.params\
                      ['ltemp6t410'].round(3))+self.asterisk_creator(\
                      reg.pvalues['ltemp6t410'])
        except:
            dictionary['Temperaturet-1/1000'] = '-'
        try:
            dictionary['  '] = '['+str(reg.std_errors['ltemp6t410']\
                       .round(3))+']'
        except:
            dictionary['  '] = '-'
        try:
            dictionary['Temperaturet+1/1000'] = str(reg.params\
            ['letemp6t410'].round(3))+ self.asterisk_creator(reg.\
            pvalues['letemp6t410'])
        except:
            dictionary['Temperaturet+1/1000'] = '-'            
        try:
            dictionary['   '] = '['+str(reg.std_errors['letemp6t410']\
                       .round(3))+']'
        except:
            dictionary['   '] = '-'
        dictionary['F-statistic of joint significance'] = reg.\
            f_statistic.stat#https://www.youtube.com/watch?v=FyRZY9Bi9n8&ab_channel=PhilChan
        dictionary['of weather variables'] = ' '
        dictionary['P-value'] = reg.f_statistic.pval
        dictionary['Observations'] = reg.nobs
        return dictionary
    
    def create_pandas_export_table_from_regs(self,reg_list,title_list=
                    ['Preferred','1-Day lag','1-Day lead','All']):
        '''
        this fct loops trough regression results and saves each one's 
        relevant numbers into a dictionary. Later these dicts are combined
        via pandas concat and transposed to match latex format. This is
        a helper function.
        '''
        export_table = pd.DataFrame([])
        for reg,index,title in zip(reg_list,
                        self.return_list_of_ascending_ints_in_brackets(
                        len(reg_list)),title_list):
            export_table = pd.concat([export_table,pd.DataFrame(
            self.return_elements_for_result_table_from_reg(reg,title),
            index= [index])],sort=False)
        export_table = pd.DataFrame(export_table)
        return  export_table.T
    
    def export_reg_results_as_latex_code(self, reg_list, filename):
        '''
        This fct only works with regression_summary_objects as elements
        in reg_list argument as we want a very specific style of table
        '''
        table = self.create_pandas_export_table_from_regs(reg_list)
        print(table)
        raw_latex = table.to_latex()
        index = raw_latex.find('Observations')
        raw_latex = raw_latex[:index] + '\midrule\n' + raw_latex[index:]
        with open(filename+'.txt', 'a') as file:
            file.write(raw_latex)
            
    def export_any_pandas_table(self, table, filename):
        '''
        This fct can export any kind of pandas table. I added some try
        and except statements to style tables with certain information
        '''
        print(table)
        raw_latex = table.to_latex()
#        index = raw_latex.find('Observations')
#        raw_latex = raw_latex[:index] + '\midrule\n' + raw_latex[index:]
        with open(filename+'.txt', 'a') as file:
            file.write(raw_latex)
            