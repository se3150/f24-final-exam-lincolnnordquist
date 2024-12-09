Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Scenario: I can successfully encode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I select "Encode" from the dropdown with id "decoder-setting"
    And I select "10" from the dropdown with id "shift-amount"
    And I input "This is a test message. Hi Jeff!" into the search field with id "letters"
    And I click button with id of "submit"
    Then I expect that the element with id "decoded_message" contains the decoded message

Scenario: I can successfully decode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I select "Decode" from the dropdown with id "decoder-setting"
    And I select "10" from the dropdown with id "shift-amount"
    And I input "Drsc sc k docd wocckqo. Rs Topp!" into the search field with id "letters"
    And I click button with id of "submit"
    Then I expect that the element with id "decoded_message" contains the encoded message
    