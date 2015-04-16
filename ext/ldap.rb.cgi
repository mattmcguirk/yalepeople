#!/usr/bin/ruby
use 'Net::LDAP';

ldap = Net::LDAP.new  :host => "galaxy.corp.com", # your LDAP host name or IP goes here,
                      :port => "389", # your LDAP host port goes here,
                      :encryption => :simple_tls,
                      :base => "DC=corp,DC=com", # the base of your AD tree goes here,
                      :auth => {
                        :method => :simple,
                        :username => "snotty@spaceball.gov", # a user w/sufficient privileges to read from AD goes here,
                        :password => "12345" # the user's password goes here
                      }
 
# GET THE DISPLAY NAME AND E-MAIL ADDRESS FOR A SINGLE USER
search_param = "lstarr"
result_attrs = ["sAMAccountName", "displayName", "mail"]
 
# Build filter
search_filter = Net::LDAP::Filter.eq("sAMAccountName", search_param)
 
# Execute search
ldap.search(:filter => search_filter, :attributes => result_attrs, :return_result => false) { |item| 
    puts "#{item.sAMAccountName.first}: #{item.displayName.first} (#{item.mail.first})"
}
