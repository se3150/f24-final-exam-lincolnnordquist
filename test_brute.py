import pytest
from brute import Brute

todo = pytest.mark.skip(reason='todo: pending spec')

def describe_Brute():

    @pytest.fixture
    def cracker():
        return Brute("TDD")
    
    def describe_init():
        def test_initializes_with_target_string():
            cracker = Brute("TDD")
            assert cracker.target == cracker.hash("TDD")
        
        def test_initializes_with_target_string_empty():
            cracker = Brute("")
            assert cracker.target == cracker.hash("")
        
        def test_it_fails_with_no_params():
            with pytest.raises(TypeError):
                Brute()
        
        def test_it_fails_with_wrong_params():
            with pytest.raises(TypeError):
                Brute(1)        

    def describe_bruteOnce():
        def test_returns_true_for_correct_attempt(cracker):
            attempt = "TDD"
            assert cracker.bruteOnce(attempt) is True

        def test_returns_false_for_wrong_attempt(cracker):
            attempt = "WRONG"
            assert cracker.bruteOnce(attempt) is False
        
        def test_returns_false_for_empty_attempt(cracker):
            attempt = ""
            assert cracker.bruteOnce(attempt) is False

    def describe_bruteMany():
        @pytest.fixture
        def stubbed_cracker(mocker):
            cracker = Brute("TDD")
            mocker.patch.object(cracker, 'randomGuess', side_effect=["WRONG", "TDD"])
            return cracker

        def test_returns_time(stubbed_cracker):
            result = stubbed_cracker.bruteMany(limit=2)
            assert result > 0

        def test_returns_negative_one(mocker):
            cracker = Brute("TDD")
            # forcing it to be wrong
            mocker.patch.object(cracker, 'randomGuess', return_value="WRONG")
            result = cracker.bruteMany(limit=2)
            assert result == -1

        def test_calls_randomGuess_and_hash_methods(mocker):
            cracker = Brute("TDD")
            mock_random_guess = mocker.patch.object(cracker, 'randomGuess', return_value="WRONG")
            mock_hash = mocker.patch.object(cracker, 'hash', wraps=cracker.hash)
            cracker.bruteMany(limit=3)
            # making sure it was called 3 times during execution
            assert mock_random_guess.call_count == 3
            assert mock_hash.call_count == 3
