package com.kata
/**
 * Created by developer on 11/12/2015.
 */

object MorseCodeDecoder {

  case class MorseTranslationTableNode (Value: String, left: Option[MorseTranslationTableNode], right: Option[MorseTranslationTableNode])

  case class MorseTranslationTableRoot (left: MorseTranslationTableNode, right: MorseTranslationTableNode)

  def decode(morseCode: String) : String = {


    val translationTree = MorseTranslationTableRoot(left = MorseTranslationTableNode("E", None, None), right = MorseTranslationTableNode("T", None, None))
    val char = morseCode(0)
    val nextSeq = morseCode.substring(1)
    val node = char match {
      case '.' => translationTree.left
      case '-' => translationTree.right
    }

    node.Value
  }
}
