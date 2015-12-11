import com.kata.MorseCodeDecoder
import org.scalatest.{Matchers, FlatSpec}

/**
 * Created by developer on 11/12/2015.
 */
class MorseCodeDecoderSpec extends FlatSpec with Matchers {

  "MorseCodeDecoder" should "decode a single characters" in {
    MorseCodeDecoder.decode(".") should === ("E")
    MorseCodeDecoder.decode("-") should === ("T")
    MorseCodeDecoder.decode(".-") should === ("A")
  }

  "MorseCodeDecoder" should "decode words" in {
    MorseCodeDecoder.decode(".- .") should === ("AE")
    MorseCodeDecoder.decode(".- .- -") should === ("AAT")
  }

  "MorseCodeDecoder" should "decode complete phrases" in {
    MorseCodeDecoder.decode(".- -   . -") should === ("AT ET")

  }

}
