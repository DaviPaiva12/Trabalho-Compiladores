// Generated from c:/Users/davip/Downloads/Compilador_calculadora-simples/Calculator.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class CalculatorLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		VAR=1, IF=2, THEN=3, ELSE=4, ASSIGN=5, SEMI=6, PLUS=7, MINUS=8, MUL=9, 
		DIV=10, LPAREN=11, RPAREN=12, REL_OP=13, ID=14, NUMBER=15, WS=16;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"VAR", "IF", "THEN", "ELSE", "ASSIGN", "SEMI", "PLUS", "MINUS", "MUL", 
			"DIV", "LPAREN", "RPAREN", "REL_OP", "ID", "NUMBER", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'var'", "'if'", "'then'", "'else'", "'='", "';'", "'+'", "'-'", 
			"'*'", "'/'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "VAR", "IF", "THEN", "ELSE", "ASSIGN", "SEMI", "PLUS", "MINUS", 
			"MUL", "DIV", "LPAREN", "RPAREN", "REL_OP", "ID", "NUMBER", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public CalculatorLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Calculator.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0010h\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n"+
		"\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\f\u0003\fL\b\f\u0001\r\u0001\r\u0005"+
		"\rP\b\r\n\r\f\rS\t\r\u0001\u000e\u0004\u000eV\b\u000e\u000b\u000e\f\u000e"+
		"W\u0001\u000e\u0001\u000e\u0004\u000e\\\b\u000e\u000b\u000e\f\u000e]\u0003"+
		"\u000e`\b\u000e\u0001\u000f\u0004\u000fc\b\u000f\u000b\u000f\f\u000fd"+
		"\u0001\u000f\u0001\u000f\u0000\u0000\u0010\u0001\u0001\u0003\u0002\u0005"+
		"\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n"+
		"\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010\u0001"+
		"\u0000\u0005\u0002\u0000<<>>\u0003\u0000AZ__az\u0004\u000009AZ__az\u0001"+
		"\u000009\u0003\u0000\t\n\r\r  p\u0000\u0001\u0001\u0000\u0000\u0000\u0000"+
		"\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000"+
		"\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b"+
		"\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001"+
		"\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001"+
		"\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001"+
		"\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001"+
		"\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001"+
		"\u0000\u0000\u0000\u0001!\u0001\u0000\u0000\u0000\u0003%\u0001\u0000\u0000"+
		"\u0000\u0005(\u0001\u0000\u0000\u0000\u0007-\u0001\u0000\u0000\u0000\t"+
		"2\u0001\u0000\u0000\u0000\u000b4\u0001\u0000\u0000\u0000\r6\u0001\u0000"+
		"\u0000\u0000\u000f8\u0001\u0000\u0000\u0000\u0011:\u0001\u0000\u0000\u0000"+
		"\u0013<\u0001\u0000\u0000\u0000\u0015>\u0001\u0000\u0000\u0000\u0017@"+
		"\u0001\u0000\u0000\u0000\u0019K\u0001\u0000\u0000\u0000\u001bM\u0001\u0000"+
		"\u0000\u0000\u001dU\u0001\u0000\u0000\u0000\u001fb\u0001\u0000\u0000\u0000"+
		"!\"\u0005v\u0000\u0000\"#\u0005a\u0000\u0000#$\u0005r\u0000\u0000$\u0002"+
		"\u0001\u0000\u0000\u0000%&\u0005i\u0000\u0000&\'\u0005f\u0000\u0000\'"+
		"\u0004\u0001\u0000\u0000\u0000()\u0005t\u0000\u0000)*\u0005h\u0000\u0000"+
		"*+\u0005e\u0000\u0000+,\u0005n\u0000\u0000,\u0006\u0001\u0000\u0000\u0000"+
		"-.\u0005e\u0000\u0000./\u0005l\u0000\u0000/0\u0005s\u0000\u000001\u0005"+
		"e\u0000\u00001\b\u0001\u0000\u0000\u000023\u0005=\u0000\u00003\n\u0001"+
		"\u0000\u0000\u000045\u0005;\u0000\u00005\f\u0001\u0000\u0000\u000067\u0005"+
		"+\u0000\u00007\u000e\u0001\u0000\u0000\u000089\u0005-\u0000\u00009\u0010"+
		"\u0001\u0000\u0000\u0000:;\u0005*\u0000\u0000;\u0012\u0001\u0000\u0000"+
		"\u0000<=\u0005/\u0000\u0000=\u0014\u0001\u0000\u0000\u0000>?\u0005(\u0000"+
		"\u0000?\u0016\u0001\u0000\u0000\u0000@A\u0005)\u0000\u0000A\u0018\u0001"+
		"\u0000\u0000\u0000BL\u0007\u0000\u0000\u0000CD\u0005=\u0000\u0000DL\u0005"+
		"=\u0000\u0000EF\u0005!\u0000\u0000FL\u0005=\u0000\u0000GH\u0005<\u0000"+
		"\u0000HL\u0005=\u0000\u0000IJ\u0005>\u0000\u0000JL\u0005=\u0000\u0000"+
		"KB\u0001\u0000\u0000\u0000KC\u0001\u0000\u0000\u0000KE\u0001\u0000\u0000"+
		"\u0000KG\u0001\u0000\u0000\u0000KI\u0001\u0000\u0000\u0000L\u001a\u0001"+
		"\u0000\u0000\u0000MQ\u0007\u0001\u0000\u0000NP\u0007\u0002\u0000\u0000"+
		"ON\u0001\u0000\u0000\u0000PS\u0001\u0000\u0000\u0000QO\u0001\u0000\u0000"+
		"\u0000QR\u0001\u0000\u0000\u0000R\u001c\u0001\u0000\u0000\u0000SQ\u0001"+
		"\u0000\u0000\u0000TV\u0007\u0003\u0000\u0000UT\u0001\u0000\u0000\u0000"+
		"VW\u0001\u0000\u0000\u0000WU\u0001\u0000\u0000\u0000WX\u0001\u0000\u0000"+
		"\u0000X_\u0001\u0000\u0000\u0000Y[\u0005.\u0000\u0000Z\\\u0007\u0003\u0000"+
		"\u0000[Z\u0001\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000][\u0001\u0000"+
		"\u0000\u0000]^\u0001\u0000\u0000\u0000^`\u0001\u0000\u0000\u0000_Y\u0001"+
		"\u0000\u0000\u0000_`\u0001\u0000\u0000\u0000`\u001e\u0001\u0000\u0000"+
		"\u0000ac\u0007\u0004\u0000\u0000ba\u0001\u0000\u0000\u0000cd\u0001\u0000"+
		"\u0000\u0000db\u0001\u0000\u0000\u0000de\u0001\u0000\u0000\u0000ef\u0001"+
		"\u0000\u0000\u0000fg\u0006\u000f\u0000\u0000g \u0001\u0000\u0000\u0000"+
		"\u0007\u0000KQW]_d\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}